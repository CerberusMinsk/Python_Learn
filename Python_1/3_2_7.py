n = int(input())

x_list = {}

while n >= 1:
    x = int(input())
    if x in x_list:
        y = x_list[x]
        print(y)
    else:
        x_list[x] = f(x)
        y = x_list[x]
        print(y)

    n -=1