from pprint import pprint
dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
'''
1. Make a copy of dist1 to result;
2. make iteration of dict2 and check if value is in resuilt:
    * if value from dict2 not in result -> add new value to result;
    * if value in dict2 -> add value from dict2 to value from result:
3. pprint(result)
'''
"""
result = {
'a': 400, 'b': 400, 'c': 312,
'd': 445, 'e': 98, 'f': 90,
'm': 230, 'q': 34, 'p': 123,
't': 853, 'w': 111, 'z': 999,
}
  """
result = dict1.copy()

for key, value in dict2.items():
    result[key] = result.get(key, 0) + value
pprint(result)




