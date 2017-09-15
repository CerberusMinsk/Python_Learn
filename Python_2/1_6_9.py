#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):
    def append(self, msg):
        super(LoggableList, self).append(msg)
        self.log(msg)


sss = LoggableList()
sss.append(5)
sss.append(101)
print(sss)
