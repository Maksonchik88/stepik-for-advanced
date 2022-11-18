n = int(input())
key_list = []
value_list = []
final_list = []

for i in range(n):
    key, value = input().split(': ')
    key_list.append(key)
    value_list.append(value)

my_dict = dict(zip(key_list, value_list))
my_dict = {k.lower(): v for k, v in my_dict.items()}

m = int(input())

for j in range(m):
    value = input().lower()
    if value not in my_dict:
        final_list.append("Не найдено")
    else:
        final_list.append(my_dict[value])

print(*final_list, sep="\n")
