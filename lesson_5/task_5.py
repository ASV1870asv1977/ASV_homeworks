"""
Задача № 5.  Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

while True:
    list_number = input('Для выхода введите "q"\n'
                        'Введите числа через пробел: ').split()
    # Проверка ввода данных
    if 'q' in list_number:
        print(f'{"-" * 50}\nВыход')
        break
    flag = None
    for i in range(len(list_number)):
        if not list_number[i].isdigit():
            print(f'{i + 1}-е значение не является цифрой\n{"=" * 50}')
            flag = 1
    if flag == 1: continue

    # Запись данных в файл
    with open('task_5.txt', 'w', encoding='utf-8') as f:
        f.write(f'{" ".join(list_number)}')
    print(f'{"-" * 50}\nФайл {f.name} записан')

    # Чтение из файла
    with open('task_5.txt', 'r') as f:
        print(f'{"-" * 50}\nФайл {f.name}:\n{f.read()}\n')
        f.seek(0)
        list_number = f.read().split()

    # Вычисление суммы чисел, находящихся в файле
    for i in range(len(list_number)):
        list_number[i] = int(list_number[i])

    print(f'Сумма чисел в файле: {sum(list_number)}\n{"=" * 50}')
