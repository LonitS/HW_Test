import random
print('Задание №7_3 \'Список чет нечёт\'')
my_list_1 = random.sample(range(1, 200), 10)
my_list_2 = random.sample(range(1, 200), 10)
my_result = []
print(f'my_list = {my_list_1}')
print(f'my_list = {my_list_2}')

for i in range(len(my_list_1)):
    if i % 2 == 0:
        my_result.append(my_list_1[i])
    else:
        my_result.append(my_list_2[i])
print(f'my_result = {my_result}')

