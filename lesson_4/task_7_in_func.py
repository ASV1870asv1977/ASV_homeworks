"""
Задача № 7.  Реализовать генератор с помощью функции с ключевым словом yield,
создающим очередное значение. При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fact(n). Функция отвечает
за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
начиная с 1! и до n!.
"""

from math import factorial


def fact_range(length):
    """
    Функция генерации очередного элемента списка числа факториала.

    :param length (int): число факториала
    :yield (int): очередной элемент списка числа факториала
    """
    for el in [i for i in range(1, length + 1)]:
        yield el


def fact_creat(val):
    """
    Функция вычисления факториала числа.

    :param val (int): число факториала
    :return (int): факториал числа
    """
    fact = 1
    if val != 0:
        for el in fact_range(val):
            fact *= el
    return fact


while True:
    fact_number = input('Введите число факториала: ')
    # Проверка ввода данных
    if fact_number == 'q': break
    try:
        fact_number = int(fact_number)
    except ValueError:
        print('Не введено целое число')
        continue

    print(f'Факториал числа {fact_number} равен {fact_creat(fact_number)}')
    print(f'Для контроля: {factorial(fact_number)}\n{"=" * 50}')
