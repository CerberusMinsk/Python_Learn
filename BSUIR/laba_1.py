import os
import re
import shutil

count = 1


def walk(dir, dir_copy):
    global count
    for name in os.listdir(dir):
        result = re.findall(r'\.txt', name)
        fln = '4_' + str(count) + '.html'
        path = os.path.join(dir, name)
        path_copy = os.path.join(dir_copy, fln)
        if os.path.isfile(path):
            if result:
                shutil.copyfile(path, path_copy)
                count = count + 1
        else:
            walk(path, dir_copy)


path = r'/home/cerberus'
folder = 'LABDIR'

project_dir = '/home/cerberus/LABDIR_COPY'  # input('DIR name: ')

fullpath = os.path.join(path, folder)
if not os.path.exists(fullpath):
    os.mkdir(fullpath)

walk(project_dir, fullpath)
lst = []

for name in os.listdir(fullpath):
    openpath = os.path.join(fullpath, name)
    lst.append(openpath)

for i in lst:
    with open(i, 'r') as inf:
        line_list = []
        line_list.append('<html><body>\n')
        for line in inf:
            for word in line.split():
                if re.match('ee', word):
                    new_line = word.replace('ee', '22', 1) + ' '
                else:
                    new_line = word + ' '
                line_list.append(new_line)
            line_list.append('\n')
        line_list.append('</html></body>\n')

    with open(i, 'w') as ouf:
        for i in line_list:
            ouf.write(i)
