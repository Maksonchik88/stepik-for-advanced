'''
Даны по 10-балльной шкале оценки по математике трех учеников.
Напишите программу, которая выводит множество оценок,
имеющихся у учеников, которые встречаются не более, чем у двух из указанных учеников.
'''

A = {int(c) for c in input().split()}
B = {int(c) for c in input().split()}
C = {int(c) for c in input().split()}

union = A.union(B).union(C)
inter = A.intersection(B).intersection(C)

res = union.difference(inter)
res = sorted(res)
print(*res)