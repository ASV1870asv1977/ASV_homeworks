"""
Задача № 2.  Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
"""

list_work = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
my_list = [list_work[i] for i in range(1, len(list_work)) if list_work[i] > list_work[i - 1]]
print(f'Результат: {my_list}')
