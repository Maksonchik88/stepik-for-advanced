n = int(input())
general_dict = dict()
for i in range(n):
    my_list = input().lower().split()
    val_list = my_list[0]
    key_list = my_list[1:]
    new_dict = dict.fromkeys(key_list, val_list)
    general_dict.update(new_dict)

m = int(input())
general_list = []
for j in range(m):
    test = input().lower()
    print(general_dict.get(test, 'Not found').title())
