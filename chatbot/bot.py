#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from .intent_detector import SCENARII
from .intent_detector.actions import TextAction


FALLBACK = TextAction("Whacchasayin' ?")
PROMPT = 'Moi©> '
HELLO = None


def wait_for_input(prompt):
    inp = None
    while not inp:
        try:
            inp = input(prompt)
        except (EOFError, KeyboardInterrupt):
            sys.exit()
    return inp


def find_scenario(text):
    for s in SCENARII:
        if s.condition.check(text):
            return s


def run(url):
    # TODO code easier to test

    if HELLO:
        HELLO.execute(url=url)

    inp = wait_for_input(PROMPT)
    scenar = find_scenario(inp)
    while not scenar:
        FALLBACK.execute(url=url)
        inp = wait_for_input(PROMPT)
        scenar = find_scenario(inp)

    cur = scenar.first_step

    while True:

        while cur.actions:
            # Pop them so they don't run twice
            cur.actions.pop(0).execute(url=url)

        if not cur.connections:
            # This is the end ...
            break

        inp = wait_for_input(PROMPT)
        for c in cur.connections:
            # Decice next step from user input
            if c.check(inp):
                cur = c.next_step
                break
        else:
            # Can't understand
            FALLBACK.execute(url=url)
