def func(st: str) -> int:
    counter = 0
    for symbol in st:
        counter += ord(symbol.upper()) - ord('A')
    return counter


lst_sort = print(*list(sorted([input() for _ in range(int(input()))], key=lambda w: (func(w), w))), sep="\n")
