# Задача 3. Универсальная программа

def some_type(iter_object):
    if isinstance(iter_object, dict):
        temp_list = [iter_object[letter] for index, letter in enumerate(iter_object) if index % 2 == 0]
    else:
        temp_list = [letter for index, letter in enumerate(iter_object) if index % 2 == 0]
    return temp_list


print('tuple: ', some_type((1, 2, 3, 4, 5, 6, 7, 8)))
print('list: ', some_type([1, 2, '3', 'a', 5, 6, 7, 8]))
print('string: ', some_type('О Дивный Новый мир!'))
print('dict: ', some_type({1: 'a', 2: 'b', 3: 'c', 4: 'd'}))
print('set: ', some_type({1, 2, 3, 4}))
