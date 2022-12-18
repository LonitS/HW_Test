def dqd(a=0):
    s = f'{a}: '
    for c in range(a):
        i = c * c
        if i <= a:
            s += f'{i} '
        else:
            break
    return s


print('Задание №2 \'Квадраты натуральных чисел\'')
digit = input('Введите число :\t')
try:
    digit = int(digit)
    x = dqd(digit)
except ValueError:
    x = 'Некоректное число'

print(x)
