#!/usr/bin/env python
# encoding: utf-8
from app.entry import Entry

__author__ = "han"


class ModelEntry(Entry):

    def __init__(self, config):
        super().__init__(config)
        self.config = config

    def run(self):
        # TODO:此处model包下要执行的模块
        for i in range(10):
            print("model entry run %s" % str(i))


class DataEntry(Entry):

    def __init__(self, config):
        super().__init__(config)
        self.config = config

    def run(self):
        # TODO:此处model包下要执行的模块
        for i in range(10):
            print("data entry run %s" % str(i))


class ClientEntry(Entry):

    def __init__(self, config):
        super().__init__(config)
        self.config = config

    def run(self):
        # TODO:此处model包下要执行的模块
        for i in range(10):
            print("client entry run %s" % str(i))
