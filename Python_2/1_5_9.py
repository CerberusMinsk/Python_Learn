#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Buffer:
    def __init__(self):
        # конструктор без аргументов
        self.lst = []

    def add(self, *a):
        # добавить следующую часть последовательности
        self.lst += [*a]
        while len(self.lst) >= 5:
            sum = 0
            for i in self.lst[:5]:
                sum = sum + i
            self.lst = self.lst[5:]
            print(sum)

    def get_current_part(self):
        # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были
        # добавлены
        return self.lst
