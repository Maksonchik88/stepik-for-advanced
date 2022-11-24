n = int(input())
my_dict = {}
for i in range(n):
    value, key = input().lower().split()
    if key not in my_dict:
        my_dict[key] = []
    my_dict[key].append(value)

m = int(input())
for j in range(m):
    query = input().lower()
    if query in my_dict:
        print(*my_dict[query])
    else:
        print('абонент не найден')
