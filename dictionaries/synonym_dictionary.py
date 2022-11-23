res = {}

for i in range(int(input())):
    key, value = input().split()
    res[key], res[value] = value, key

word = input()
syn = res.get(word)
print(syn)