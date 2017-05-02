glb = [{'parent': 'None', 'namespace': 'global', 'var': []}]


def add(namespace, var):
    for i in glb:
        if namespace == i.get('namespace'):
            i.get('var').append(var)
            # print(i.get('var'))


def create(namespace, parent):
    glb.append({'parent': parent, 'namespace': namespace, 'var': []})


def get(namespace, var):
    global temp
    for i in range(len(glb)):
        if namespace == glb[i].get('namespace'):
            temp = glb[i]
    if namespace == temp.get('namespace'):
        if var in temp.get('var'):
            print(temp.get('namespace'))
            return 0
        else:
            return get(temp.get('parent'), var)
    else: print('None')


n = int(input())

for i in range(n):
    cmd, nmsp, var = input().split()

    if cmd == 'add':
        add(nmsp, var)
    elif cmd == 'create':
        create(nmsp, var)
    elif cmd == 'get':
        get(nmsp, var)
