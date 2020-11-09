"""
Задача № 3.  Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""

def my_max(number1, number2, number3):
    """
    Функция принимает три позиционных аргумента, формирует из них список,
    удаляет наименьший и возвращает сумму оставшихся двух аргументов.

    :param number1 (float): первый аргумент
    :param number2 (float): второй аргумент
    :param number3 (float): третий аргумент

    :return (float): сумма наибольших двух аргументов
    """
    my_list = [number1, number2, number3]
    my_list.remove(min(my_list))
    return sum(my_list)

while True:
    print('Сумма двух больших чисел.\nДля выхода нажмите "q"')

    n = None  # Контрольная переменная для повтора программы
    print('-' * 50)
    my_list = input('Введите три числа через пробел: ').split()

    # Проверка правильности ввода данных
    if 'q' in my_list or 'й' in my_list:
        print('Выход')
        break

    if len(my_list) < 3 or len(my_list) > 3:
        print(f'Количество введенных чисел не равно трем!\n{"=" * 50}')
        continue

    for i in range(len(my_list)):
        try:
            my_list[i] = float(my_list[i])
        except ValueError:
            print(f'Не введено численное значение {i + 1}-го числа\n{"=" * 50}')
            n = 1  # Контрольное значение для повтора программы
            break
    if n == 1: continue

    a, b, c = my_list
    print(f'Суумма двух наибольших чисел равна: {round(my_max(a, b, c), 2)}\n{"=" * 50}')

