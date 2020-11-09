"""
Задача № 4.  Программа принимает число x и целое число y. Необходимо выполнить
возведение числа x в степень y. Задание необходимо реализовать в виде
функции my_func(x, y). При решении задания необходимо обойтись без встроенной
функции возведения числа в степень.
"""

def elevate_gen(number1, number2):
    """
    Функция принимает два позиционных аргумента и возвращает
    результат возведения первого аргумента в степень второго.

    :param number1 (float): первый аргумент
    :param number2 (int): второй аргумент

    :return (float): результат возведения в степень
    """

    elevate = abs(number2)
    res = 1
    for i in range(1, elevate + 1):
        res = res * number1
    if number2 < 0:
        res = 1 / res
    return res

while True:
    print('Cтепень числа.\nДля выхода нажмите "q"')
    print('-' * 50)
    number1 = input('Введите число, возводимое в степень: ')
    if number1 == 'q' or number1 == 'q':
        print('Выход')
        break
    number2 = input('Введите степень числа (целое число): ')
    if number2 == 'q' or number2 == 'q':
        print('Выход')
        break
    # Проверка правильности ввода данных
    try:
        number1 = float(number1)
        number2 = int(number2)
    except ValueError:
        print(f'{"-" * 50}\nВвод данных не соответствует условиям\n{"=" * 50}')
        continue

    print(f'{"-" * 50}\n{number1} в степени {number2} равно: {elevate_gen(number1, number2)}')
    print(f'Для контроля: {number1 ** number2}\n{"=" * 50}')


