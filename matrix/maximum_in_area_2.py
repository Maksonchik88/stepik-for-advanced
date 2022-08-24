# Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.




n = int(input())

matrix = []

for _ in range(n):
    temp = [int(c) for c in input().split()]
    matrix.append(temp)

lst = []
for i in range(n):
    for j in range(n):
        if (i >= j and i + j + 1 <= n) or (i <= j and i + j + 1 >= n):
            lst.append(matrix[i][j])
print(max(lst))