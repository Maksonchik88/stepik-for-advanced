from functools import reduce

def evaluate(coefficients, x):
    return reduce(lambda p, a: p * x + a, coefficients)


iter = list(map(int, input().split()))
num = int(input())
print(evaluate(iter, num))