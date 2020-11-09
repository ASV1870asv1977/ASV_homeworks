"""
Задача № 3.  Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""
seasons_list = ['зима', [12, 1, 2], 'весна', [3, 4, 5], 'лето', [6, 7, 8], 'осень', [9, 10, 11]]
seasons_dict = {'зима': [12, 1, 2],
                'весна': [3, 4, 5],
                'лето': [6, 7, 8],
                'осень': [9, 10, 11]}
season = None
while True:                                       # Ввод данных
    print('-' * 50)
    month = input('Для выхода нажмите "q"\nВведите месяц в виде целого числа от 1 до 12: ')
    if month == 'q' or month == 'й':
        break

    try:                                          # Обработка ошибок ввода пользователя
        month = int(month)
    except ValueError:
        print('Не введено целое число!')
        continue
    if month > 12 or month < 1:
        print('Введено число не соответствуещее диапазону!')
        continue

    # Реализация с помощью списка
    for i in range(0, len(seasons_list), 2):
        if month in seasons_list[i+1]:
            print(f'\nРеализация с помощью списка.\nВремя года: {seasons_list[i]}')

    # Реализация с помощью словаря
    for season, months in seasons_dict.items():
        if month in months:
            print(f'\nРеализация с помощью словаря.\nВремя года: {season}')
