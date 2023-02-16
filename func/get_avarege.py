numbers = [(10, -2, 3, 4), (-13, 56), (1, 9, 2), (-1, -9, -45, 32), (-1, 5, 1), (17, 0, 1), (0, 1), (3,), (39, 12),
           (11, -23), (10, -100, 21, 32), (3, -8), (1, 1)]



def get_avarege(tup: tuple) -> int:
    return sum(tup) / len(tup)


sorted_numbers = sorted(numbers, key=lambda tup: get_avarege(tup), reverse=True)

print(sorted_numbers)