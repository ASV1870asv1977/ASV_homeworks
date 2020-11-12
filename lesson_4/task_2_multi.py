"""
Задача № 2.  Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.

Пользователь вводит количество элементов списка list_len и диапазон значений списка user_range.
Выводится элементы исходного списка, значения которых больше предыдущего элемента.
"""

from random import randint

while True:
    list_len = input('Для выхода нажмите "q"\nВведите количество элементов списка: ')
    if list_len == 'q': break
    list_len = int(list_len)
    user_range = input('Введите диапазон списка\n'
                       '(два целочисленных значения через пробел): ').split()
    # Генерация списка с указанными входными параметрами
    list_work = [randint(int(user_range[0]), int(user_range[1])) for i in range(list_len)]

    print(f'{"-" * 50}\nСписок из {list_len} случайных элементов от {int(user_range[0])} '
          f'до {int(user_range[1])}:\n{list_work}')

    # Генерация списка в соответствии с условием задачи
    my_list = [list_work[i] for i in range(1, len(list_work)) if list_work[i] > list_work[i - 1]]

    print(f'Результат: {my_list}\n{"=" * 50}')
