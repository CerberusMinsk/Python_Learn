import os
import re
import shutil


sss = 1

def coppy(dir):
    print(dir)



def walk(dir, dir_copy):
    global sss
    for name in os.listdir(dir):
        result = re.findall(r'\.txt', name)
        fln = '4_' + str(sss) + '.html'
        path = os.path.join(dir, name)
        path_copy = os.path.join(dir_copy, fln)
        if os.path.isfile(path):
            if result:
                shutil.copyfile(path, path_copy)
                sss = sss + 1
                print(sss)
                #coppy(name)

        else:
            walk(path, dir_copy)


# os.rename(r"ttt.py", r'test1.py') #переименование файла
path = r'/home/cerberus'
folder = 'LABDIR'

project_dir = input('DIR name: ')

fullpath = os.path.join(path, folder)
if not os.path.exists(fullpath):
    os.mkdir(fullpath)

walk(project_dir, fullpath)
