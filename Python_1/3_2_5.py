def update_dictionary(d, key, value):
    lst = []
    if key in d:
        lst = d.get(key)
        lst.append(value)

    elif (key * 2) in d:
        lst = d.get(key*2)
        lst.append(value)

    else:
        d.setdefault(key * 2, [value])

d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)                            # {2: [-1, -2, -3]}