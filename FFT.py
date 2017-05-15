import math

Wre = []
Wim = []
new_list = []
N = 64


def Wkoef(i, N, Wre, Wim):
    Wre.append(math.cos(2 * math.pi * i / N))
    Wim.append(- math.sin(2 * math.pi * i / N))


for i in range(int(N / 2)):
    Wkoef(i, N, Wre, Wim)
    new_list.append([round(Wre[i], 3), round(Wim[i], 3)])

with open('Wkoef.txt', 'w', encoding='utf8') as ouf:
    for i in new_list:
        print(i, file=ouf)
        print(i)
