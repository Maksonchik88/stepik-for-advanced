data = {}
for line in range(int(input())):
    buyer, goods, number = input().split()
    if buyer not in data:
        data[buyer] = {goods: int(number)}
    else:
        if goods not in data[buyer]:
            data[buyer][goods] = int(number)
        else:
            data[buyer][goods] += int(number)

data_sort = sorted(data.items(), key=lambda x: x[0])

for name, goods_buyer in data_sort:
    print(name, ':', sep='')
    goods_buyer_sort = sorted(goods_buyer.items(), key=lambda x: x[0])
    for goods, buyer in goods_buyer_sort:
        print(goods, buyer)





