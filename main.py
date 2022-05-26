import json

from faker import Faker
fake_ru = Faker('ru_RU')

dict = {}

for i in range (1,250):
    name = fake_ru.name()
    tn = fake_ru.phone_number()
    j = fake_ru.job()
    A = fake_ru.address()
    dict[i] = {name:[A, j, tn]}
    with open ("DS.txt", 'w', encoding='utf-8') as f:
        json.dump(dict, f, indent = 4, ensure_ascii = False)

# import csv
#
# fake_ru = Faker('ru_RU')
#
# # filepath = "C:\Users\Marlit\PycharmProjects\pythonProject1.csv"
# # with open(filepath) as f:
#
# with open("file.csv", mode="w", encoding='utf-8') as file:
#     for i in range(2):
#         w = csv.writer(file, delimiter=",", lineterminator="\r")
#         w.writerow(fake_ru.name(), fake_ru.phone_number(), fake_ru.job(), fake_ru.address())
#         # w.writerow(fake_ru.phone_number())
#         # w.writerow(fake_ru.job())
#         # w.writerow(fake_ru.address())


