res = {}

for i in range(int(input())):
    key, value = input().split()
    res[key], res[value] = value, key    

print(res[input()])