"""
Задача № 6.  Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного;
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Выход из итерации осуществляется вызовом метода .is_pressed() модуля keyboard
"""

import keyboard
from itertools import count, cycle

while True:
    number = input('Сгенерировать целые числа            => 1\n'
                   'Сгенерировать повторяющиеся элементы => 2\n'
                   'Выход                                => 3\n'
                   'Выбирите действие: ')
    print('-' * 50)

    if number == '1':
        start = int(input('Для остановки нажмите "q"\nВведите начальное число генерации: '))
        i = 0
        for el in count(start):
            if keyboard.is_pressed('q'):
                print(f'Стоп. Произведено {i} итераций\n{"=" * 50}')
                break
            i += 1
            print(el)

    if number == '2':
        element = input('Для остановки нажмите "q"\nВведите элементы для повторения: ')
        i = 0
        for el in cycle(element):
            if keyboard.is_pressed('q'):
                print(f'Стоп. Произведено {i} итераций\n{"=" * 50}')
                break
            i += 1
            print(el)

    if number == '3':
        break
