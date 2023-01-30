from typing import List

def get_matrix(a=None, b=None, c=None) -> List[List[int]]:
    if a is None:
        return [[0]]
    elif a is not None and b is None and c is None:
        return [[0] * a for _ in range(a)]
    elif a is not None and b is not None and c is None:
        return [[0] * b for _ in range(a)]
    else:
        return [[c] * b for _ in range(a)]


p = get_matrix(3, 4, 9)
print(p)
