res = {}

for i in range(int(input())):
    key, value = input().split()
    res[key], res[value] = value, key    

key_word = input()

if key_word not in res:
    print(None)
else:
    print(res[key_word])