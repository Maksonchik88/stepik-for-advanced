my_list = input().split()
print(*list(sorted(my_list, key=lambda st: str(st).lower())))