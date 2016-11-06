n = int(input())
mtrx = [[0 for j in range(n)] for i in range(n)]
num = 1
x = 0
y = 0
y_end = n
x_end = n
kfc = 1
while num <= n ** 2:

    while y < x_end:
        mtrx[x][y] = num
        num += 4
        y += kfc




for i in range(n):
    for j in range(n):
        print(mtrx[i][j], end=' ')
    print()