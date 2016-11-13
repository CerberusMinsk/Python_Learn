#lst = [i for i in input().split()]
lst = ['a', 'aa', 'abC', 'aa', 'ac', 'abc', 'bcd', 'a']
lst_2 = {}
print(lst)

for i in range(len(lst)):
    lst_2[(lst[i].lower())] = 1

print(lst_2.keys[0])