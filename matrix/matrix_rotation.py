# Напишите программу, которая поворачивает квадратную матрицу чисел на 90^  по часовой стрелке.


from typing import List


def rotate(mat:List[List[int]]) -> List[List[int]]:
    m = len(mat)
    n = len(mat[0])
    mat2 = [[0] * m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            mat2[j][m - i - 1] = mat[i][j]
    return mat2




n = int(input())

mtx1 = [list(map(int, input().split(' '))) for _ in range(n)]
mtx2 = rotate(mtx1)

for row in mtx2:
    print(' '.join(map(str, row)))

