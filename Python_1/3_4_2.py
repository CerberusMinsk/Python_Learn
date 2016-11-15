a_z = [str(i) for i in range(0, 10)]
lst = []
new_lst = []
kfc = 1
cifra = ''

with open('dataset_3363_2.txt', 'r', encoding='utf8') as inf:
    with open('reply_3363_2.txt', 'w', encoding='utf8') as ouf:
        for line in inf:
            lst = list(line)

            for i in range(len(lst)):
                if lst[i] in a_z:
                    cifra = cifra + lst[i]
                    kfc = int(cifra)
                else:
                    new_lst.append(lst[i])
                    kfc = 1
                    cifra = ''

                ins = new_lst.pop(-1)
                new_lst.append(ins * kfc)

            for i in new_lst:
                ouf.write(i)
