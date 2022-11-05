from pprint import pprint
s = 'orange strawberry barley gooseberry apple apricot barley currant orange ' \
    'melon pomegranate banana banana orange barley apricot plum grapefruit banana ' \
    'quince strawberry barley grapefruit banana grapes melon strawberry apricot currant c' \
    'urrant gooseberry raspberry apricot currant orange lime quince grapefruit barley ' \
    'banana melon pomegranate barley banana orange barley apricot plum banana quince ' \
    'lime grapefruit strawberry gooseberry apple barley apricot currant orange melon ' \
    'pomegranate banana banana orange apricot barley plum banana grapefruit banana quince ' \
    'currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'


'''
{'apple': 2,
 'apricot': 7,
 'banana': 12,
 'barley': 12,
 'currant': 6,
 'gooseberry': 3,
 'grapefruit': 6,
 'grapes': 1,
 'lime': 3,
 'melon': 5,
 'orange': 8,
 'plum': 4,
 'pomegranate': 5,
 'quince': 5,
 'raspberry': 1,
 'strawberry': 4}
'''
my_list = s.split()
# print(my_list)
my_dict = {}
for word in my_list:
    if word not in my_dict:
        my_dict[word] = 0
    my_dict[word] += 1
# pprint(my_dict)

max_word, max_count = my_dict.popitem()
# print(max_word, max_count)


for current_word, current_count in my_dict.items():
    max_count = max(current_count, max_count)
    if current_count == max_count:
        max_word = min(max_word, current_word)
print(max_word)


