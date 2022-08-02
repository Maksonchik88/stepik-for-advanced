lst = []
lst1 = input().split()
n = int(input())
for i in range(0, len(lst1), n):
    lst.append(lst1[i: i + n])
print(lst)