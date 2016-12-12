import requests
cnt = 0
with open('dataset_3378_2.txt', 'r') as inf:
    url = inf.read().strip()
print(url)
r = requests.get(url)

lst = r.text.splitlines()
print(len(lst))
