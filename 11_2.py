file_name = input('Введите имя файла:\t')
file_read = open(f'{file_name}.txt', "r")
text = file_read.read()
text = text.lower()
words = text.split()
words = [word.strip('.,!;()[]') for word in words]
words = [word.replace("'s", '') for word in words]
unique = list(set(words))
unique.sort()
total = {}
for u in unique:
    total[u] = text.count(u)
cis = 0
for i, j in total.items():
    if cis < 5:
        print(f'[{i}: {j}]', end='')
        cis += 1
    else:
        print()
        cis = 0
