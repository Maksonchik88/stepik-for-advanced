'''
Даны по 10-балльной шкале оценки по физике трех учеников.
Напишите программу, которая выводит множество оценок третьего ученика,
которые не встречаются ни у первого, ни у второго ученика.
'''


A = {int(c) for c in input().split()}
B = {int(c) for c in input().split()}
C = {int(c) for c in input().split()}

union_A_B = A | B
res = C.difference(union_A_B)

print(*sorted(res, reverse=True))