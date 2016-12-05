n = int(input())
lst = {}

def command_add (com, lst):
    if com in lst:
        lst[com][0] += 1
    else:
        lst[com] = [1, 0, 0, 0, 0]

def winners (com_1, com_2, gol_1, gol_2):
    if gol_1 > gol_2:
        com_1[1] +=1
    elif gol_1 == gol_2:
        com_1[2] += 1
        com_2[2] += 1
    else:
        com_2[1] += 1



for i in range(n):
    str = [i for i in input().split(';')]

    command_add(str[0], lst)
    command_add(str[2], lst)
    winners(lst[str[0]], lst[str[2]], str[1], str[3])

print(str)
#lst['Зенит'][1]=3
for key, value in lst.items():
    print(key, value)