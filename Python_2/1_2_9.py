res = []
for obj in objects:

    if id(obj) not in res:
        res.append(id(obj))

print(len(res))
