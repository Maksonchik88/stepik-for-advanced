#Следом квадратной матрицы называется сумма элементов главной диагонали.
# Напишите программу, которая выводит след заданной квадратной матрицы.



n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)
res = 0
for j in range(len(matrix)):
    res += matrix[j][j]

print(res)