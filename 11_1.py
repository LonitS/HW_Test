import re
file_name = input('Введите имя файла:\t')
raw_words = input('Введите слова для замены через пробел:\t')
file_read = open(f'{file_name}.txt', "r")
lines = file_read.readlines()
print('_' * 100)
print(raw_words.split())
for line in lines:
    for word in raw_words.split():
        reg_exp = r'\b' + word + r'\b'
        line = re.sub(reg_exp, '*' * len(word), line, count=0, flags=re.IGNORECASE)
    print(line[:-1])
print('_' * 100)
