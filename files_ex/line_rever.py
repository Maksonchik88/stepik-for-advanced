with open("files_ex/text.txt") as file:
    for line in file:
        l = line[::-1]
        print(l)