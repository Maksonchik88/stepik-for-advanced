from pprint import pprint
s = input()
s = s.lower()
for i in '.,!?:;-':
   s = s.replace(i, '')

# print(s)

my_list = s.split()
# print(my_list)

my_dict = {}

for word in my_list:
    if word not in my_dict:
        my_dict[word] = 0
    my_dict[word] += 1
# pprint(my_dict)

min_word, min_count= my_dict.popitem()

for current_word, current_count in my_dict.items():
    min_count = min(current_count, min_count)
    if current_count == min_count:
        min_word = min(min_word, current_word)
print(min_word)
