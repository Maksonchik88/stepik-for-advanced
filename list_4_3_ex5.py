text = input().split()

result = [[text[0]]]

for i in range(1, len(text)):
    if text[i] == text[i - 1]:
        result[-1].extend(text[i])
    else:
        result.append([text[i]])
print(result)