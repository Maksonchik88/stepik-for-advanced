n = 8  # лучше запихнуть число в перемнную для удобства
horse = input()

row = n - int(horse[1])  # переводим координаты строки на питоний
col = ord(horse[0]) - 97  # переводим координаты столбца на питоний с помощью ord()

mtx = [['.'] * n for _ in range(n)]  # создаем матрицу и заполняем ее точками

mtx[row][col] = 'N'

for di in (-2, +2):  # конь ходит влево и вправо на два и вверх или низ на один
    for dj in (-1, +1):
        i = row + di
        j = col + dj
        if 0 <= i < n and 0 <= j < n:
            mtx[i][j] = '*'

for dj in (-2, +2):  # конь ходит вверх и низ на два и вправо и лево на один
    for di in (-1, +1):
        i = row + di
        j = col + dj
        if 0 <= i < n and 0 <= j < n:
            mtx[i][j] = '*'

for row in mtx:
    print(' '.join(row))