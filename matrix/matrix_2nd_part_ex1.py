
'''На вход программе подаются два натуральных числа n и m — количество строк и столбцов в матрице.
Создайте матрицу mult размером n x m заполните её таблицей умножения по формуле mult[i][j] = i * j. '''


n, m = int(input()), int(input())
mult = [[str(i * j).ljust(3) for i in range(m)] for j in range(n)]

print(*[''.join(k) for k in mult], sep='\n')
