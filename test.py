#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from chatbot import bot

if __name__ == '__main__':

    url = False

    try:
        if sys.argv[1] == '--http':
            url = sys.argv[2]
    except IndexError:
        pass

    bot.run(url)
