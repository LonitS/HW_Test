def tr_a(high=5):
    for i in range(high):
        print(int((high - i)) * ' ', (i * 2 + 1) * '*', sep='')


def tr_b(high=5):
    print(high * ' ', '*', sep='')
    for i in range(high - 2):
        print(int((high - i - 1)) * ' ', '*', (i * 2 + 1) * ' ', '*', sep='')
    print(int((high - i - 2)) * ' ', (high * 2 - 1) * '*', sep='')


def tr_c(high=5):
    tr_a(high)
    for i in reversed(range(high - 2)):
        print(int((high - i - 1)) * ' ', '*', (i * 2 + 1) * ' ', '*', sep='')
    print(high * ' ', '*', sep='')


def tr_d(high=5):
    tr_a(high)
    for i in reversed(range(high - 2)):
        print(int((high - i - 1)) * ' ', '*', int((i * 2 + 1) / 2) * ' ', '*', int((i * 2 + 1) / 2) * ' ', '*', sep='')
    print(high * ' ', '*', sep='')


print('Задание №5_2 \'Треугольники\'')
n_high = input('Высота треугольника:\t')
try:
    n_high = int(n_high)
    if n_high < 3:
        print('Введите число больше чем 2!')
        n_high = 3
    for i in 'ABCD':
        print(i)
        locals()[f'tr_{i.lower()}'](n_high)
except ValueError:
    print('Некоректное число')
