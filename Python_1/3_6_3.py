import requests

with open('dataset_3378_3.txt', 'r') as inf:
    url = inf.read().strip()

r = requests.get(url)
lst = r.text.splitlines()

while lst[0][0] != 'W':
    url = 'https://stepic.org/media/attachments/course67/3.6.3/' + lst[0]
    r = requests.get(url)
    lst = r.text.splitlines()

print(r.text)
