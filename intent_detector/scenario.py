#!/usr/bin/env python
# -*- coding: utf-8 -*-


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
