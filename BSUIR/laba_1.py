import os
import re
import shutil

def coppy(dir):
    print(dir)


def walk(dir, dir_copy):
  for name in os.listdir(dir):
    path = os.path.join(dir, name)
    path_copy = os.path.join(dir_copy, name)
    if os.path.isfile(path):
        shutil.copyfile(path, path_copy)
        coppy(name)

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






