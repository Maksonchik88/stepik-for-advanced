from math import sin


def square(num: int) -> int:
    return num ** 2


def cube(num: int) -> int:
    return num ** 3


def radical(num: int) -> float:
    return num ** 0.5


def module(num: int) -> int:
    return abs(num)


def sinus(num: int):
    return sin(num)


data = {"квадрат": square, "куб": cube, "корень": radical, "модуль": module, "синус": sinus}

n = int(input())
command = input()
print(data[command](n))
