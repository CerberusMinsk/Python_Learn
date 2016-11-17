'''Решение полный отстой :('''
lst = []
lst_2 = []
wrd = {}
x = 0
prnt = []
prnt_2 = ''

with open('dataset_3363_3.txt', 'r') as inf:
    with open('reply_3363_3.txt', 'w') as ouf:
        for line in inf:
            lst.append(line.lower().split())

        for i in range(len(lst)):
            lst_2 += lst[i][:]

        for i in range(len(lst_2)):
            if lst_2[i] in wrd.keys():
                wrd[lst_2[i]] += 1
            else:
                wrd[lst_2[i]] = 1

        for key in wrd.keys():
            if wrd[key] > x:
                prnt = [key, wrd[key]]
                x = wrd[key]

        prnt_2 = prnt[0] + " " + str(prnt[1])
        print(prnt_2)


        ouf.writelines(prnt_2)

