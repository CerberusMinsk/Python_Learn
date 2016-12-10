val_str = input()
key_str = input()
encrypt_str = input()
decrypt_str = input()
encr_lst = {}
decr_lst = {}

for i in range(len(key_str)):
    encr_lst[val_str[i]] = key_str[i]
    decr_lst[key_str[i]] = val_str[i]

encStr = ''

for i in encrypt_str:
    encStr += encr_lst[i]

decStr = ''
for i in decrypt_str:
    decStr += decr_lst[i]

print(encStr)
print(decStr)
