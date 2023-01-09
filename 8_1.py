
persons = [{"name": "John", "age": 15}, {"name": "Samm", "age": 22}, {"name": "Jack111", "age": 45},
           {"name": "John2", "age": 16}, {"name": "Samm2", "age": 22}, {"name": "Jack111", "age": 44},
           {"name": "John3", "age": 17}, {"name": "Samm3", "age": 22}, {"name": "Jack111", "age": 43},
           {"name": "John4", "age": 18}, {"name": "Samm4", "age": 22}, {"name": "Jack111", "age": 42}]
list_1 = []
list_2 = []
old = 1000
name_len = ""
mid = 0
for person in persons:
    if len(person["name"]) > len(name_len):
        name_len = person["name"]
    if person["age"] < old:
        old = person["age"]
    mid += person["age"]
mid = mid/len(persons)
for person in persons:
    if person["age"] == old:
        list_1.append(person["name"])
    if person["name"] == name_len:
        list_2.append(person["name"])

print('Задание №8_1 \'Самые молодые\'')
print("A:")
print(list_1)
print("B:")
print(list_2)
print("C:")
print(mid)
