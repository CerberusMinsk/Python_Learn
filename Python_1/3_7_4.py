n = int(input())
in_str = []
x = 0
y = 0
for i in range(n):
    in_str = input().split()

    if in_str[0] == 'север':
        y += int(in_str[1])
    elif in_str[0] == 'юг':
        y -= int(in_str[1])
    elif in_str[0] == 'восток':
        x += int(in_str[1])
    elif in_str[0] == 'запад':
        x -= int(in_str[1])

print(x, y)
