my_list = [1, 2, 3, 4, 5]
my_dict = {1: 'one', 2: 'two', 3: 'three'}

for element in my_list:
    if element not in my_dict:
        my_list.remove(element)

print(my_list)  