import os

br = 'y'
print('Hillel 4')
while br.lower() == 'y':
    numb_1 = input('Номер домашнего (4, 5):\t')
    numb_2 = input('Номер задания (1,2,3):\t')
    try:

        # if 0 < int(numb_2) < 4 and 3 < int(numb_1) < 6:
            os.system(f'python {numb_1}_{numb_2}.py')
        # else:
        #     print('Некоректный номер')
    except ValueError:
        print('Некоректное число')

    br = input('Хотите посмотреть следующее задание? \'y\'\t')
