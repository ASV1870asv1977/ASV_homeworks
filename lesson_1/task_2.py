"""
Задача № 2
Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""
while True:
    time_sec = input('Для выхода нажмите "q"\nВведите время в секундах: ')
    if time_sec == 'q' or time_sec == 'й':
        break
    time_sec = int(time_sec)
    time_min = time_sec // 60
    time_hour = time_sec // 3600
    time_sec = time_sec - (time_min * 60)
    time_min  = time_min - (time_hour * 60)

    list_time = [time_hour, time_min, time_sec]

    i = 0
    while i < len(list_time):                     # Преобразование в str для добавления "0"
        list_time[i] = str(list_time[i])
        if len(list_time[i]) == 1:
            list_time[i] = '0' + list_time[i]
        i += 1

    print(f'Ваше время: {list_time[0]}.{list_time[1]}.{list_time[2]}')
    print('-' * 50)





