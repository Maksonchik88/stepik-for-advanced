# На вход программе подаются два натуральных числа nn и mm. Напишите программу для создания матрицы размером n×m, заполнив её символами .
# и * в шахматном порядке.
# В левом верхнем углу должна стоять точка. Выведите полученную матрицу на экран, разделяя элементы пробелами.

# создаем матрицу
n, m = [int(c) for c in input().split()]
mtx = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if (i + j) % 2 == 0:
            mtx[i][j] = '.'
        else:
            mtx[i][j] = '*'

for k in range(n):
    for r in range(m):
        print(mtx[k][r], end=' ')
    print()