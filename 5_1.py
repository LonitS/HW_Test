print('Задание №5_1 \'Числа до 100\'')
sp = '0123456789'

for i in sp:
    for j in sp:
        print(f'{i}{j}', sep=",", end=" ")
    print()
