b = open('lines.txt', 'r', -1, 'utf-8')
b1 = set(b.readlines())
print(b1.pop())
b.close()
