"""
Задача № 6.  Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара
и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
"""
data_base = []                                          # Список для представления требуемой структуры
my_data_base = []                                       # Список для формирования базы данных
print('Данные по товарам отсутствуют')
i = 1
while True:


    while i > 0:                                        # Цикл для формирования базы товаров
        print('=' * 50)

        # Ввод данных в базу
        choice = input('Добавить товар в базу? y/n: ')
        if choice == 'n' or choice == 'т':
            break
        if choice == 'y' or choice == 'н':
            name = input('Введите название товара: ')

            while True:
                price = input('Введите цену товара: ')
                try:
                    price = float(price)
                    break
                except ValueError:
                    print('Не введено численное значение цены товара!')
                    continue
            while True:
                quantity = input('Введите количество товара: ')
                try:
                    quantity = int(quantity)
                    break
                except ValueError:
                    print('Не введено целочисленное значение количества товара!')
                    continue
            unit = input('Введите единицу измерения товара: ')

            print(f'{("-"*50)}\nВ базе {i} товар(ов):')
            product = {'название': name, 'цена': price, 'количество': quantity, 'единица измерения': unit}
            my_data_base.append(product)
            for j in range(len(my_data_base)):
                print(f"{j+1}. {my_data_base[j]['название']}, цена {my_data_base[j]['цена']},"
                      f" {my_data_base[j]['количество']} {my_data_base[j]['единица измерения']}")
        i += 1
    # Формирования требуемой структуры базы товаров
    for my_data in enumerate(my_data_base, 1):
        data_base.append(my_data)
    print(f'Требуемая структура данных:\n{data_base}')

    # Аналитика о товарах
    analytic_dict = {}                                  # Словарь требуемого формата
    data_list_name = []                                 # Списки со значениями словаря
    data_list_price = []
    data_list_quantity = []
    data_list_unit = []

    for category in data_base:                          # Обход структуры базы товаров
        data_list_name.append(category[1]['название'])
        analytic_dict['название'] = list(set(data_list_name))
        data_list_price.append(category[1]['цена'])
        analytic_dict['цена'] = list(set(data_list_price))
        data_list_quantity.append(category[1]['количество'])
        analytic_dict['количество'] = list(set(data_list_quantity))
        data_list_unit.append(category[1]['единица измерения'])
        analytic_dict['единица измерения'] = list(set(data_list_unit))

    print(f'{("*" * 50)}\nТребуемый формат реализации анализа:\n{analytic_dict}')
    print(f'{("*" * 50)}\n'
          f'Категория товаров в базе данных: {analytic_dict["название"]}\n'
          f'Цены на товары: {analytic_dict["цена"]}\n'
          f'Единицы измерения товаров: {analytic_dict["единица измерения"]}')

    print('*' * 50)
    choice = input('Продолжить работу с базой? y/n: ')
    if choice == 'n' or choice == 'т':
        break
    if choice == 'y' or choice == 'н':
        analytic_dict.clear()                                      # Очищение данных по анализу
        data_list_name.clear()
        data_list_price.clear()
        data_list_quantity.clear()
        data_list_unit.clear()
        continue