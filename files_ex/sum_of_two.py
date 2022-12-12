a = open('numbers.txt')
lst = a.readlines()
lst_n = []
for line in lst:
    line = line.rstrip()
    lst_n.append(int(line))
print(sum(lst_n))
a.close()
