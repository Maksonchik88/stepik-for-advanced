'''
Даны по 10-балльной шкале оценки по биологии трех учеников.
Напишите программу, которая выводит множество оценок,
не встречающихся ни у одного из трех учеников.
'''


A = {int(c) for c in input().split()}
B = {int(c) for c in input().split()}
C = {int(c) for c in input().split()}
test = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

union = A | B | C

res = test.difference(union)
print(*sorted(res))

