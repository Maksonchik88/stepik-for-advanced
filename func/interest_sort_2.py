def sum_num(num: int) -> int:
    count = 0
    num = str(num)
    for n in num:
        count += int(n)
    return count


lst = list(map(int, input().split()))
lst.sort()
print(*sorted(lst, key=sum_num))