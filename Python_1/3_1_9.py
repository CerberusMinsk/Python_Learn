lst = [1, 2, 3, 4, 5, 6]

def modify_list(l):
    lst_2 = l[:]
    del l[:]
    lenght = len(lst_2)
    for i in range(0,lenght):
        if (lst_2[i] % 2) == 0:
            l.append(int(lst_2[i] / 2))


print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4]