#!/usr/bin/python
# -*- coding: utf-8 -*-

class MoneyBox:
    def __init__(self, capacity):
        # конструктор с аргументом – вместимость копилки
        self.capacity = capacity
        self.volume = 0

    def can_add(self, v):
        # True, если можно добавить v монет, False иначе
        if (self.volume + v) <= self.capacity:
            return True
        else:
            return False

    def add(self, v):
        # положить v монет в копилку
        if self.can_add(v):
            self.volume += v
