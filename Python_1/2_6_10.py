#('2_6_10')
mtrx = []
inpt = True
lst = []
while inpt:
    lst = (input().split())
    if lst != ['end']:
        mtrx.append(lst)
    else:
        break

row = len(mtrx)
col = len(mtrx[0])
#print(row)
#print(col)
for i in range(row):
    for j in range(col):
        print(mtrx[i][j], end=' ')
    print()