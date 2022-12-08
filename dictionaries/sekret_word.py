code = input()
my_dict = {}
for el in code:
    my_dict.setdefault(code.count(el), el)

for _ in range(int(input())):
    key, value = input().split(':')
    code = code.replace(my_dict[int(value)], key)
print(code)

