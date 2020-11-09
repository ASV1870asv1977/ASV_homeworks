"""
Задача № 3
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""
while True:
    number = input('Для выхода нажмите "q"\nВведите целое число: ')
    if number == 'q' or number == 'й':
        break
    sum_str = ''                                # Переменная для конкатенации
    sum = 0                                     # Переменная для суммы
    i = 1
    while i < 4:
        sum_str = sum_str + number
        sum = sum + int(sum_str)
        i += 1

    print(f'Сумма чисел в формате "n + nn + nnn" равна: {sum}')
    print('-' * 50)
