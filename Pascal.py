n = int(input()) + 1
pas = []
for i in range(n):
    row = []
    for j in range(i + 1):
        if j == 0 or i == j:
            row.append(1)
        else:
            row.append(pas[i - 1][j - 1] + pas[i - 1][j])
    pas.append(row)
print(row)
