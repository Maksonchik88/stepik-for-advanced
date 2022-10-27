key_list = [i for i in range(1, 16)]
value_list = [(j**2) for j in key_list]
result = dict(zip(key_list, value_list))
print(result)