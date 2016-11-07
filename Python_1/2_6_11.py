n = int(input())
mtrx = [[0 for j in range(n)] for i in range(n)]
num = 1
x = 0
y = 0
y_end = 0
x_end = 0
kfc = 1
while num <= n ** 2:

    while y < n:
        mtrx[x][y] = num
        num += 4
        y += 1

    x_end += 1
    y -= 1
    while x_end < n:
        mtrx[x_end][y] = num
        num += 4
        x_end += 1




for i in range(n):
    for j in range(n):
        print(mtrx[i][j], end=' ')
    print()