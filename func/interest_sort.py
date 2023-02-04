def sum_num(num: int) -> int:
    count = 0
    for n in num:
        count += int(n)
    return count

lst = input().split()
sort_lst = sorted(lst, key=sum_num)
print(*sort_lst)

