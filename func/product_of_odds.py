from functools import reduce


def product_of_odds(data: list):
    return reduce(lambda x, y: x * y, filter(lambda a: a % 2 == 1, data), 1)


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(product_of_odds(lst))
