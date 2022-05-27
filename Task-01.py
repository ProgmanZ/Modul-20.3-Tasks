# Задача 1. Саботаж!

user_string = input('Строка: ')
for index, letter in enumerate(user_string):
    if letter == '~':
        print(index, end=' ')
