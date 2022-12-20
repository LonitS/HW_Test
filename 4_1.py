def add(n=0, m=0):
    return n + m


def subs(n=0, m=0):
    return n - m


def prod(n=0, m=0):
    return n * m


def div(n=1, m=1):
    return n / m


def rem(n=1, m=1):
    return n % m


def operations(op, n, m):
    try:
        n = int(n)
        m = int(m)
    except ValueError:
        return "Ошибка!\n" \
               "Введите числа корректно"

    switch = {
        '+': add(n, m),
        '-': subs(n, m),
        '*': prod(n, m),
        '/': div(n, m),
        '%': rem(n, m),
    }
    return switch.get(op, 'Ошибка!\nВведите оператор корректно: +,-,*,/,%')


print('Задание №1 \'Калькулятор\'1')
a = input('Первое число:\t')
b = input('Второе число:\t')
o = input('Введите один из операторов (+,-,*,/,%):\t')
x = operations(o, a, b)
print(f'{a} {o} {b} = {x}')
