"""
Задача № 6.  Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного;
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
"""

from itertools import count, cycle

while True:
    number = input('Сгенерировать целые числа            => 1\n'
                   'Сгенерировать повторяющиеся элементы => 2\n'
                   'Выход                                => 3\n'
                   'Выбирите действие: ')

    if number == '1':
        start = int(input('Введите начальное число генерации: '))
        for el in count(start):
            if el > 100:
                break
            print(el)

    if number == '2':
        element = input('Введите элементы для повторения: ')
        i = 0
        for el in cycle(element):
            if i > 10:
                break
            print(el)
            i += 1

    if number == '3':
        break