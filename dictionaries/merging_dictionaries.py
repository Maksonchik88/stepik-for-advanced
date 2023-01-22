def merge(values):
    result = {}
    for dicts in values:
        for key, value in dicts.items():
            if key not in result:
                result[key] = set()
                result[key].add(value)
            else:
                result[key].add(value)
    return result

print(merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}]))