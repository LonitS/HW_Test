print('Задание №7_11 \'Уникальные символы из строки\'')
my_str = '123232321567880'
my_result = []
exec("""\nfor i in list(my_str):\n\t if list(my_str).count(i) == 1:\n\t\t  my_result.append(i)\n""")
print(f'my_str = {my_str}')
print(f'my_result = {my_result}')
