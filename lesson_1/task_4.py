"""
Задача № 4
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""
while True:
    number = input('Для выхода нажмите "q"\nВведите целое положительное число: ')
    if number == 'q' or number == 'й':
        break

    max_number = int(number[0])
    min_number = int(number[0])
    i = 1
    while i < len(number):
        if int(number[i]) > max_number:
            max_number = int(number[i])
        if int(number[i]) < min_number:
            min_number = int(number[i])
        i += 1

    print(f'Наибольшая цифра: {max_number}')
    print(f'Наименьшая цифра: {min_number}')
    print('-' * 50)