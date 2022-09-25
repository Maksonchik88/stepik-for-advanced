# Напишите программу для определения общего количества различных слов в строке текста.

words = [word.lower().strip('.,;:-?!') for word in input().split()]
print(words)

print(len(set(words)))
