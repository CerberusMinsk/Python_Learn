keys = [i for i in range(1, 12)]
temp_str = []
prnt_dict = {k: '-' for k in keys}
cnt_dict = {k: 0 for k in keys}

with open('dataset_3380_5.txt', 'r', encoding='utf-8') as f:
    for line in f:
        temp_str.append(line.split())

for i in range(len(temp_str)):
    if prnt_dict[int(temp_str[i][0])] == '-':
        prnt_dict[int(temp_str[i][0])] = int(temp_str[i][2])
    else:
        prnt_dict[int(temp_str[i][0])] += int(temp_str[i][2])

for i in range(len(temp_str)):
    cnt_dict[int(temp_str[i][0])] += 1

for i in range(1, 12):
    print(i, prnt_dict[i] / cnt_dict[i])
