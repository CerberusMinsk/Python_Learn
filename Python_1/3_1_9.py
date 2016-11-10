lst = [1, 2, 3, 4, 5, 6]

def modify_list(l):
    lenght = len(l)
    for i in range(0,lenght):

        if (l[i] % 2) != 0:
            l.pop(i)
            lenght -= 1



print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4]