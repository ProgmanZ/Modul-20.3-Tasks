# Задача 2. Словари из списков

import random


def string_generator(user_dict):
    return [user_dict[random.randint(0, len(user_dict))] for _ in range(10)]


dict_alpha = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


first_list = string_generator(dict_alpha)
second_list = string_generator(dict_alpha)

first_dict = {index: letter for index, letter in enumerate(first_list)}
second_dict = {index: letter for index, letter in enumerate(second_list)}

print('Первый список:', first_list)
print('Второй список:', second_list)

print('\nПервый словарь:', first_dict)
print('Второй словарь:', second_dict)
