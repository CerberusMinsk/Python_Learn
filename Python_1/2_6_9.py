lst = [i for i in input().split()]
x = input()

cnt = True
g = 0
for i in range(len(lst)):
    if lst[i] == x:
        print(i, end=' ')
        cnt = False
if cnt:
    print('Отсутствует')
