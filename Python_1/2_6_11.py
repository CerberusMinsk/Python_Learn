n = int(input())
mtrx = [[0 for j in range(n)] for i in range(n)]
num = 1
x = 0
y = 0
kfc = 1
XX = 0
YY = 0
while num <= n ** 2:

    for i in range(YY, n):
        mtrx[x][y] = num
        y += kfc
        num += 1
    y += kfc * (-1)
    x += kfc
    XX += 1

    for i in range(XX, n):
        mtrx[x][y] = num
        x += kfc
        num += 1

    x += kfc * (-1)
    kfc *= (-1)
    y += kfc
    YY += 1

for i in range(n):
    for j in range(n):
        print(mtrx[i][j], end=' ')
    print()
