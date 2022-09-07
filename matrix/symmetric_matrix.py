n = int(input())
mtx = [[int(i) for i in input().split()] for _ in range(n)]

flag = True
for i in range(n):
    for j in range(n):
        if mtx[i][j] != mtx[j][i]:
            flag = False
            break

if flag:
    print('YES')
else:
    print('NO')