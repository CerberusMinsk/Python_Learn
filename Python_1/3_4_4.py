lst = []
mathim = 0
phizik = 0
russian = 0
cnt = 0
sr_ball = 0

with open('dataset_3363_4.txt', 'r', encoding='utf8') as inf:
    with open('reply_3363_4.txt', 'w', encoding='utf8') as ouf:
        for line in inf:
            lst = list(line.strip().split(';'))
            mathim += int(lst[1])
            phizik += int(lst[2])
            russian += int(lst[3])
            sr_ball = (int(lst[1]) + int(lst[2]) + int(lst[3]))/3
            ouf.write(str(sr_ball) + '\n')
            cnt += 1
        mathim = (mathim / cnt)
        phizik = (phizik / cnt)
        russian = (russian / cnt)

        ouf.write(str(mathim) + ' ' + str(phizik) + ' ' + str(russian))
