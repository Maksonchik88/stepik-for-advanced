n = int(input())
general_dict = dict()
for i in range(n):
    my_list = input().split()
    val_list = my_list[0]
    key_list = my_list[1:]
    new_dict = dict.fromkeys(key_list, val_list)
    general_dict.update(new_dict)

m = int(input())
general_list = []
for j in range(m):
    test = input().title()
    if test.isalpha():
        general_list.append(general_dict[test])
    else:
        None

for el in general_list:
    print(el)

