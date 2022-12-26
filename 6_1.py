import random


def prh(ls):
    print('print_100 = ', end='')
    for i in ls:
        if i > 100:
            print(f'{i}, ', end='')
    print('\n')


def lsh(ls):
    print('list_100 = ', end='')
    result_list = []
    for i in ls:
        if i > 100:
            result_list.append(i)
    print(f'{result_list}\n')


def lss(ls):
    print('list if 2 = ', end='')
    ls_copy = ls.copy()
    len_ls = len(ls_copy)
    if len_ls >= 2:
        ls_copy.append(ls_copy[len_ls - 1] + ls_copy[len_ls - 2])
    else:
        ls_copy.append(0)
    print(f'{ls_copy}\n')


def ls_pop(ls):
    print(f'my_list = {ls}')
    index = int(input('Введите индекс: '))
    print(f'index for del = {ls[index]}')
    for i in range(index, len(ls) - 1):
        ls[i] = ls[i + 1]
    ls.pop(len(ls) - 1)
    print(f'pop index from list = {ls}\n')


def ls_append(ls):
    print(f'my_list = {ls}')
    index = int(input('Введите индекс: '))
    value = int(input('Введите Значение: '))
    ls.append(0)
    for i in reversed(range(index, len(ls) - 1)):
        ls[i + 1] = ls[i]
    ls[index] = value
    print(f'append index in list = {ls}\n')


def ls_uniq(ls):
    ls_s = random.sample(range(1, 200), 15)
    print(f'my_list = {ls}\n len = {len(ls)}')
    print(f'my_list_2 = {ls_s}\n len = {len(ls_s)}')
    ls.extend(ls_s)
    print('uniq = ', len(dict(zip(ls, [ls.count(i) for i in ls]))))


print('Задание №6_1 \'Списки\'')
my_list = random.sample(range(1, 200), 15)
print(f'my_list = {my_list}\n')
prh(my_list)
lsh(my_list)
lss(my_list)
ls_pop(my_list)
ls_append(my_list)
ls_uniq(my_list)
