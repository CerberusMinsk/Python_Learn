glb = [{'parent':'None', 'namespace':'global', 'var':''}]

def add (namespace, var):
    for i in glb:
        if namespace == i.get('namespace'):
            i['var'] = var
            #print(i.get('var'))

def create (namespace, parent):
    glb.append({'parent':parent, 'namespace':namespace, 'var':''})

def get (namespace, var):
  for i in range(len(glb)):
    if namespace == glb[i].get('namespace'):
      temp = glb[i]
  if namespace == temp.get('namespace'):
    if var == temp.get('var'):
      print(temp.get('namespace'))
      return 0
    elif temp.get('parent') == 'None' and var != temp.get('var'):
      print('None')
      return 0
    else:
      return get(temp.get('parent'), var)

n = int(input())

for i in range(n):
    a = input().split()

    if a[0] == 'add':
        add(a[1], a[2])
    elif a[0] == 'create':
        create(a[1], a[2])
    elif a[0] == 'get':
        get(a[1], a[2])
