glb = []

def add (nspc, var):
    print(nspc, var)
    if nspc == 'global':
        glb.append(var)
    else:
        pass
    return 0

i = input().split()

if i[0] == 'add':
    print('add')
    add(i[1],i[2])


print(glb)
