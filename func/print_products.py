def print_products(*args):
    counter = 0
    for elem in args:
        if type(elem) is str and len(elem) != 0:
            counter += 1
            print(f'{counter})', elem)

    if counter == 0:
        print('Нет продуктов')



print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)