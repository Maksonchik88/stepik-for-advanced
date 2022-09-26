'''
Даны по 10 -балльной шкале оценки по информатике трех учеников.
Напишите программу, которая выводит множество оценок, которые есть и у
первого и у второго учеников, но которых нет у третьего ученика
 '''
A = {int(c) for c in input().split()}
B = {int(c) for c in input().split()}
C = {int(c) for c in input().split()}

res = A.intersection(B)

res.difference_update(C)
print(*sorted(res, reverse=True))