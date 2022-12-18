import os

br = 'y'
print('Hillel 4')
while br.lower() == 'y':
    n = input('Номер задания (1,2,3):\t')
    try:
        n = int(n)
        if 0 < n < 4:
            os.system(f'python 4_{n}.py')
        else:
            print('Некоректное число')
    except ValueError:
        print('Некоректное число')

    br = input('Хотите посмотреть следующее задание? \'y\'\t')
