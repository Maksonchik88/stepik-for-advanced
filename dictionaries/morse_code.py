letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..',
         '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-',
         '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']
# my_dict = {letters[i]: morse[i] for i in range(len(letters))}
my_dict = {}
for i in range(len(letters)):
    key = letters[i]
    value = morse[i]
    my_dict [key] = value
# print(my_dict)

word = input().upper()

my_list = []
for sym in word:
    if sym in my_dict:
        el = my_dict[sym]
        my_list.append(el)

# print(*my_list, sep=' ')
print(' '.join((j) for j in my_list))