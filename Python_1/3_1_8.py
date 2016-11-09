a = float(input())

def func(x):
    if x <= -2:
        f = 1 - (x + 2) ** 2
        return f
    elif (-2 < x) and (x <= 2):
        f = -x / 2
        return f
    elif 2 < x:
        f = (x - 2) ** 2 +1
        return f

print(func(a))