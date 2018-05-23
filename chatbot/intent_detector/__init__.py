#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .actions import TextAction, ImageAction
from .scenario import Condition, Connection, Scenario, Step


SCENARII = (
    Scenario(
        'Hi',
        'Hello',
        Step(
            'Howdy',
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
    ),
)
