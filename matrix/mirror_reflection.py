# Дана квадратная матрица чисел. Напишите программу, которая зеркально отображает её элементы относительно горизонтальной оси симметрии.


n = int(input())

mtx = [[int(i) for i in input().split()]for _ in range(n)]
mtx2 = mtx[::-1]
for i in range(len(mtx2)):
    for j in range(len(mtx2)):
        print(mtx2[i][j], end=' ')
    print()


