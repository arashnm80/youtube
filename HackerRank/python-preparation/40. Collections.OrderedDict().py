from collections import OrderedDict

N = int(input())
my_ordered_dict = OrderedDict()

for i in range(N):
    line = input().split()
    item_price = int(line[-1])
    item_name = " ".join(line[:-1])
    if item_name in my_ordered_dict:
        my_ordered_dict[item_name] += item_price
    else:
        my_ordered_dict[item_name] = item_price
        
for key in my_ordered_dict:
    print(key, my_ordered_dict[key])
