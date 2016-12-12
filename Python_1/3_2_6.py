lst = [i for i in input().split()]

lst_2 = {}

for i in range(len(lst)):
    var_item = lst[i].lower()
    if var_item in lst_2:
        lst_2[var_item] += 1
    else:
        lst_2[var_item] = 1

key_list = list(lst_2.keys())
value_list = list(lst_2.values())

for i in range(len(key_list)):
    print(key_list[i], value_list[i])
