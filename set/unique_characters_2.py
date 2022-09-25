# Напишите программу для вывода общего количества уникальных символов во всех считанных словах без учета регистра.
n = int(input())
myset = set()
for _ in range(n):
    float_set = set(input().lower())
    myset |= float_set

print(len(myset))
