def is_prime(number: int) -> bool:
    """ Возвращает True, если number - это простое число
    """
    assert number > 1
    return all(number % i for i in range(2, int(number**0.5) + 1))

def is_fibonacci(number: int) -> bool:
    """ Возвращает True, если number - это число Фибоначчи
    """
    assert number > 1
    a, b = 0, 1
    while a + b < number:
        a, b = b, a + b
    return a + b == number

# Множество простых чисел до 100
primes = set(filter(is_prime, range(2, 101)))

# Множество чисел Фибоначчи до 100
fibonacci = set(filter(is_fibonacci, range(2, 101)))

# Множество простых чисел до 100, которые одновременно являются
# числами Фибоначчи
prime_fibonacci = primes.intersection(fibonacci)

# Или используя оператор `&`, который определён для множеств
prime_fibonacci = fibonacci & primes

print(prime_fibonacci)

# Вывод (порядок может быть другим):
# {2, 3, 5, 13, 89}