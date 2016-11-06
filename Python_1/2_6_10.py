#('2_6_10')
mtrx = []
mtrx_2 = []
inpt = True
lst = []
a = 0
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
mtrx_2 = [[0 for j in range(col)] for i in range(row)]

for i in range(row):
    if (i + 1) >= row:
        i_r = -1
    else:
        i_r = i
    for j in range(col):
        if (j + 1) >= col:
            j_r = -1
        else:
            j_r = j
        mtrx_2[i][j] = int(mtrx[i][j - 1]) + int(mtrx[i - 1][j])
        mtrx_2[i][j] += int(mtrx[i][j_r + 1]) + int(mtrx[i_r + 1][j])



for i in range(row):
    for j in range(col):
        print(mtrx_2[i][j], end=' ')
    print()
