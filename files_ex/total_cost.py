a = open('prices.txt')
b = [i for i in a.read().split('\n')]
lst = list()
for line in b:
    line = line.split()
    lst.append(line)

total = 0
for el in lst:
    if len(el) == 3:
        total += (int(el[2]) * int(el[1]))

print(total)

a.close()