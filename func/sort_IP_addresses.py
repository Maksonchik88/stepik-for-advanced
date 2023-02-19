k = int(input())
lst = [input() for _ in range(k)]

lst_sort = list(sorted(lst, key=lambda st: tuple(map(int, st.split('.')))))

for tp in lst_sort:
    print(tp)
