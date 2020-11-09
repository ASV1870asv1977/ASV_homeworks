"""
Задача № 2.  Реализовать функцию, принимающую несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных
о пользователе одной строкой.
"""

def uers_processing(name, surname, year, city, e_address, tel):
    """
    Функция принимает параметры, описывающие данные пользователя как именованные
    аргументы, запаковывает их в список, реализовывает вывод данных о пользователе
    одной строкой через пробел.

    :param name (str): имя
    :param surname (str): фамилия
    :param year (str): год рождения
    :param city (str): город проживания
    :param e_address (str): email
    :param tel (str): телефон
    :return (str): данные о пользователе
    """
    return ' '.join([name, surname, year, city, e_address, tel])

while True:
    print("=" * 50)
    user_dict = {
            'имя': None,
            'фамилию': None,
            'год рождения': None,
            'город': None,
            'email': None,
            'телефон': None}

    for key in user_dict:
        user_dict[key] = input(f'Введите {key} пользователя: ')

    res = uers_processing(name=user_dict['имя'], surname=user_dict['фамилию'], year=user_dict['год рождения'], city=user_dict['город'], e_address=user_dict['email'], tel=user_dict['телефон'])
    print(f'{"=" * 50}\n{res}')

    choice = input(f'{"-" * 50}\nДля выхода введите "q"\nДля продолжения любое значение: ')
    if choice == 'q' or choice == 'й':
        print(f'{"-" * 50}\nВыход')
        break



