"""
Задача № 5.  Реализовать формирование списка, используя функцию range() и возможности
генератора. В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
"""

from functools import reduce


def multi_el(prev_el, el):
    """
    Функция умножения элементов списка.

    :param prev_el (int): предыдущий элемент
    :param el (int): текущий элемент
    :return (int): произведение параметров
    """
    return prev_el * el


my_list = [val for val in range(100, 1001) if val % 2 == 0]
print(my_list)
print(reduce(multi_el, my_list))
