#!/usr/bin/env python

import sys


# Could be a Step subclass
class Scenario:

    def __init__(self, name, trigger, step):
        self.first_step = step
        self.name = name
        self.condition = Condition(trigger)


class Step:

    def __init__(self, name, actions, *connections):
        self.name = name
        self.actions = actions
        self.connections = connections


class Connection:

    def __init__(self, next, condition=None):
        self.next_step = next
        self.condition = condition

    def check(self, text):
        return self.condition is None or self.condition.check(text)


class Condition:

    def __init__(self, string, exact=True):
        self.string = string
        self.exact = exact

    def check(self, text):
        if self.exact:
            return text == self.string
        else:
            return text in self.string


class Action:

    def execute(self, *args, **kwargs):
        raise NotImplemented("This is the base class. Use a subclass instead.")


class TextAction(Action):

    def __init__(self, text):
        super().__init__()
        self.text = text

    def execute(self):
        print('Rho Bot>', self.text)


class ImageAction(Action):

    def __init__(self, url):
        super().__init__()
        self.url = url

    def execute(self):
        print('Rho Bot>', f'(sending image: {self.url})')


if __name__ == '__main__':
    only_s = Scenario(
        'Howdy',
        'Hello',
        Step(
            'Hi',
            [TextAction('Hi, how are you ?')],
            Connection(
                condition=Condition('Fine'),
                next=Step(
                    'Cool',
                    [TextAction('Cool')]
                )
            ),
            Connection(
                condition=Condition('sad', False),
                next=Step(
                    'Ask why',
                    [TextAction('Why?')],
                    Connection(
                        next=Step(
                            'Brighten day',
                            [TextAction('Here is something to brighten your day :'),
                             ImageAction('https://i.imgur.com/4QvA1xc.gif')]
                            )
                    )
                )
            )
        )
    )

    FALLBACK = TextAction("Whacchasayin' ?")

    scenars = [only_s]
    cur = None
    prompt = 'Moi©> '

    def wait_for_input(prompt):
        inp = None
        while not inp:
            try:
                inp = input(prompt)
            except (EOFError, KeyboardInterrupt):
                sys.exit()
        return inp

    while not cur:
        inp = wait_for_input(prompt)
        for s in scenars:
            if s.condition.check(inp):
                cur = s.first_step
                break
        else:
            FALLBACK.execute()

    while True:

        while cur.actions:
            cur.actions.pop(0).execute()

        if not cur.connections:
            break

        inp = wait_for_input(prompt)
        for c in cur.connections:
            if c.check(inp):
                cur = c.next_step
                break
        else:
            FALLBACK.execute()
