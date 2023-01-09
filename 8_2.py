my_dict_1 = {1: 1, 2: 2}
my_dict_2 = {11: 11, 2: 22}
list_1 = []
list_2 = []
my_dict_3 = {}
my_dict_4 = {}
for key, value in my_dict_1.items():
    if key in my_dict_2:
        list_1.append(key)
    else:
        list_2.append(key)
        my_dict_3 = {key: value}

for key in (my_dict_1.keys() | my_dict_2.keys()):
    if key in my_dict_1: my_dict_4.setdefault(key, []).append(my_dict_1[key])
    if key in my_dict_2: my_dict_4.setdefault(key, []).append(my_dict_2[key])

print('Задание №8_1 \'Самые молодые\'')
print("A:")
print(list_1)
print("B:")
print(list_2)
print("C:")
print(my_dict_3)
print("D:")
print(my_dict_4)
