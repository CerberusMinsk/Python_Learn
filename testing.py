col = 5
row = 5
mtrx_2 = [[0 for j in range(col)] for i in range(row)]
print(mtrx_2)
print()
mtrx_2 [2][1] = 1
mtrx_2 [2][2] = 9
print(mtrx_2)
print()
for i in range(row):
    for j in range(col):
        print(mtrx_2[i][j], end=' ')
    print()

print()
for i in range(9, 3, -1):
    print(i, end=' ')