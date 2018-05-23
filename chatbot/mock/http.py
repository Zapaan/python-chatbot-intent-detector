#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
from random import random


def post(url, body):
    sleep(random())
    print('Sending into outer space ... : ', body)
