glb = [{'parent':'None', 'namespace':'global', 'var':''}]

def add (namespace, var):
    for i in glb:
        if namespace == i.get('namespace'):
            i['var'] = var
            #print(i.get('var'))

def create (namespace, parent):
    glb.append({'parent':parent, 'namespace':namespace, 'var':''})

def get (namespace, var):
   for i in glb:
       if namespace == i.get('namespace'):
           if var == i.get('var'):
               print(i.get('namespace'))
               break
           elif i.get('parent') == 'None':
               if var != i.get('var'):
                   if a[1] == 'global':
                       print('global')
                   else:
                       print('None')

           else:
               get(i.get('parent'), var)

n = int(input())

for i in range(n):
    a = input().split()

    if a[0] == 'add':
        add(a[1], a[2])
    elif a[0] == 'create':
        create(a[1], a[2])
    elif a[0] == 'get':
        get(a[1], a[2])
