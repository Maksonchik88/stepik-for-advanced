# Напишите программу, которая выводит количество элементов квадратной матрицы в каждой строке,
# больших среднего арифметического элементов данной строки.



n = int(input())
matrix = []
for _ in range(n):
    elem = [int(c) for c in input().split()]
    matrix.append(elem)

for elem in matrix:
    total = 0
    for i in elem:
        if i > (sum(elem) / len(elem)):
            total += 1
    print(total)