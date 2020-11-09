"""
Задача № 6
Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
"""
while True:
    distance = input('Для выхода нажмите "q"\nВведите результат пробежки за первый день, км: ')
    if distance == 'q' or distance == 'й':
        break
    distance_wish = input('Введите желаемый результат дневной пробежки, км: ')
    if distance_wish == 'q' or distance_wish == 'й':
        break
    distance = float(distance)
    distance_wish = int(distance_wish)

    days = 1                                                # Порядковый номер дня
    dist_every = distance                                   # Ежедневная дистанция
    while dist_every <= distance_wish:
        print(f'{days}-й день:{round(dist_every, 2)} км')
        dist_every = dist_every + dist_every * 0.1
        days +=1
    print(f'{days}-й день:{round(dist_every, 2)} км')
    print('.' * 50)
    print(f'На {days}-й день спортсмен достигнет результата не менее {distance_wish} км')
    print('=' * 50)