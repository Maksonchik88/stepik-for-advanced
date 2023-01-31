def mean(*args):
    counter = 0
    sum_num = 0
    for val in args:
        if type(val) is int or type(val) is float:
            counter += 1
            sum_num += val
    if counter > 0:
        return sum_num / counter
    else:
        return 0.0


print(mean())
print(mean(7))
print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
print(mean(True, ['stepik'], 'beegeek', (1, 2)))
print(mean(-1, 2, 3, 10, ('5')))
print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
