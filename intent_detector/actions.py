#!/usr/bin/env python
# -*- coding: utf-8 -*-


class BaseAction:

    def execute(self, *args, **kwargs):
        raise NotImplemented("This is the base class. Use a subclass instead.")


class TextAction(BaseAction):

    def __init__(self, text):
        super().__init__()
        self.text = text

    def execute(self):
        print('Rho Bot>', self.text)


class ImageAction(BaseAction):

    def __init__(self, url):
        super().__init__()
        self.url = url

    def execute(self):
        print('Rho Bot>', f'(sending image: {self.url})')
