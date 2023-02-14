a = int(input())
b = int(input())
my_lst = list(filter(lambda x: '0' not in x, [str(i) for i in range(a, b + 1)]))

def check_num(st: str) -> int:
    if len(st) == 1:
        return int(st)
    else:
        if all(int(st) % int(x) == 0 for x in st):
            return int(st)


filter_lst = print(*list(map(int, (filter(check_num, my_lst)))))
