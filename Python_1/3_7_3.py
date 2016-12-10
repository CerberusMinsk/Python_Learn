n = int(input())
word_lst = []
prnt_lst = []
for i in range(n):
    word_lst.append(input().lower())

l = int(input())
str_lst = []
for i in range(l):
    str_lst.append(input().lower().split())

for i in range(len(str_lst)):
    for j in range(len(str_lst[i])):
        if str_lst[i][j] not in word_lst:
            if str_lst[i][j] not in prnt_lst:
                prnt_lst.append(str_lst[i][j])

for i in prnt_lst:
    print(i)
