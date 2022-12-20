from random import random
from math import sqrt


#
# def mul(a, b, m):
#     q = a * b / m
#     r = a * b - q * m
#     return (r + 5 * m) % m
#
#
# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)
#
#
# def pows(a, b, m):
#     if b == 0:
#         return 1
#     if b % 2 == 0:
#         t = pows(a, b / 2, m)
#         return mul(t, t, m) % m
#     return mul(pows(a, b - 1, m), a, m) % m
#
#
# def ferma(x):
#     if x == 2:
#         return True
#     for i in range(100):
#         a = (random() % (x - 2)) + 2
#         if gcd(a, x) != 1:
#             return False
#         if pows(a, x - 1, x) != 1:
#             return False
#     return True


def simple(a):
    i = 2
    while i <= sqrt(a):
        i += 1
        if a % i == 0:
            return False
    return True


print('Задание №3 \'Простые числа (Простой метод и Ферма)\'')
digit = input('Введите число :\t')
try:
    digit = int(digit)
    result = simple(digit)
    # result = ferma(digit)
except ValueError:
    result = 'Некоректное число'
print(f'Числo {digit}: {result}')
