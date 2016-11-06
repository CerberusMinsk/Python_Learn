col = 3
row = 4
mtrx_2 = [[0 for j in range(col)] for i in range(row)]
print(mtrx_2)
mtrx_2 [1][2] = 1
print(mtrx_2)
for i in range(row):
    for j in range(col):
        print(mtrx_2[i][j], end=' ')
    print()