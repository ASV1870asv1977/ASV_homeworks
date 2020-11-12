"""
Задача № 7.  Реализовать генератор с помощью функции с ключевым словом yield,
создающим очередное значение. При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fact(n). Функция отвечает
за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
начиная с 1! и до n!.
"""

from math import factorial


def fact_range(val):
    """
    Функция генерации очередного элемента списка числа факториала.

    :param val (int): число факториала
    :yield (int): очередной элемент списка числа факториала
    """
    for el in [i for i in range(1, val + 1)]:
        yield el


while True:
    fact_number = input('Для выхода нажмите "q"\nВведите число факториала: ')
    # Проверка ввода данных
    if fact_number == 'q': break
    try:
        fact_number = int(fact_number)
    except ValueError:
        print('Не введено целое число')
        continue

    # Вычисление факториала числа
    fact = 1
    if fact_number != 0:
        for el in fact_range(fact_number):
            fact *= el

    print(f'Факториал числа {fact_number} равен {fact}')
    print(f'Для контроля: {factorial(fact_number)}\n{"=" * 50}')
