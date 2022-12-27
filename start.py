import os

br = 'y'
print('Hillel 4')
while br.lower() == 'y':
    numb_1 = input('Номер домашнего (4-7):\t')
    numb_2 = input('Номер задания:\t')
    try:
        os.system(f'python {numb_1}_{numb_2}.py')
    except ValueError:
        print('Некоректное число')

    br = input('Хотите посмотреть следующее задание? \'y\'\t')
