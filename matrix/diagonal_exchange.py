n = int(input())
mtx = [[int(c) for c in input().split()] for _ in range(n)]
for i in range(len(mtx)):
    temp = mtx[i][i]
    mtx[i][i] = mtx[n - 1 - i][i]
    mtx[n - 1 - i][i] = temp


for j in range(len(mtx)):
    for k in range(len(mtx)):
        print(mtx[j][k], end=' ')
    print()