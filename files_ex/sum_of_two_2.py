a = open('nums.txt')
b = [i for i in a.read().split()]
lst = []
for line in b:
    lst.append(int(line))
print(sum(lst))
a.close()