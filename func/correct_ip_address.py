ip = input().split('.')
print(all(map(lambda x: x.isdigit() and int(x) <= 255, ip)))
