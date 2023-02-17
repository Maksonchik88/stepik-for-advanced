lst = []
for i in range(int(input())):
    st = tuple(map(int, input().split('.')))
    lst.append(st)

lst_sort = list(sorted(lst, key=lambda st: (st[0], st[1], st[2], st[3])))

for tp in lst_sort:
    tp = '.'.join(map(str, tp))
    print(tp)