"""
Задача № 1.  Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

def my_division(divddend, divider):
    """
    Функция делит два числа

    :param divddend (float): первое число
    :param divider (float): второе число
    :return (float or None): Частное двух чисел
    """
    return divddend / divider

print('Деление двух чисел.\nДля выхода нажмите "q"')
while True:
    n = None  # Контрольная переменная для повтора программы
    print('-' * 50)
    my_list = input('Введите два числа через пробел: ').split()

    # Проверка правильности ввода данных
    if 'q' in my_list or 'й' in my_list:
        print('Выход')
        break

    if len(my_list) < 2 or len(my_list) > 2:
        print('Количество введенных чисел не равно двум!')
        continue

    for i in range(len(my_list)):
        try:
            my_list[i] = float(my_list[i])
        except ValueError:
            print(f'Не введено численное значение {i+1}-го числа')
            n = 1                    # Контрольное значение для повтора программы
            break
    if n == 1: continue

    if my_list[1] == 0:
        print('Деление на ноль не допускается')
        continue

    print(f'Частное чисел равно: {round(my_division(my_list[0], my_list[1]), 2)}')