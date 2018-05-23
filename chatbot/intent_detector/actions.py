#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ..mock import http


class BaseAction:

    def execute(self, url=None):
        if url:
            self.execute_remotely(url=url)
        else:
            self.execute_locally()

    def execute_locally(self, *args, **kwargs):
            raise NotImplemented("This is the base class. Use a subclass instead.")

    def execute_remotely(self, *args, **kwargs):
            raise NotImplemented("This is the base class. Use a subclass instead.")


class TextAction(BaseAction):

    def __init__(self, text):
        super().__init__()
        self.text = text

    def execute_locally(self, **kwargs):
        print('Rho Bot>', self.text)

    def execute_remotely(self, **kwargs):
        http.post(kwargs['url'], f'Rho Bot> {self.text}')


class ImageAction(BaseAction):

    def __init__(self, url):
        super().__init__()
        self.url = url

    def execute_locally(self, **kwargs):
        print('Rho Bot>', f'(sending image: {self.url})')

    def execute_remotely(self, **kwargs):
        http.post(kwargs['url'], f'Rho Bot> (sending image: {self.url})')
