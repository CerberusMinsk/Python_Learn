#!/usr/bin/python3
# -*- coding: utf-8 -*-


def srch(chek_lst):
    rang_list = []
    if len(chek_lst) > 0:
        for i in range(len(chek_lst)):
            if chek_lst[i] not in check and chek_lst[i] != 'None':
                check.add(chek_lst[i])
                rang_list += d[chek_lst[i]]
        return srch(rang_list)
    else:
        return 0


d = dict()
n = int(input())
while n > 0:
    lst = list(input().split(' '))

    lst_value = []
    if len(lst) > 1:
        for i in lst[1:]:
            if i != ' ' and i != ':':
                lst_value.append(i)
    else:
        lst_value.append('None')

    d[lst[0]] = lst_value
    n -= 1

q = int(input())
while q > 0:
    all_lst = []
    check = set()
    predok, potomok = input().split(' ')
    if predok == potomok:
        print('Yes')
    else:
        all_lst += d[potomok]
        srch(all_lst)
        if predok in check:
            print('Yes')
        else:
            print('No')

    q -= 1
