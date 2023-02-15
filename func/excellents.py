total = 0
num = int(input())
for i in range(num):
    temp = []
    for j in range(int(input())):
        _, ball = input().split()
        ball = int(ball)
        if ball == 5:
            temp.append(ball)
    if len(temp) > 0:
        total += 1

print( 'YES' if total == num else 'NO')



