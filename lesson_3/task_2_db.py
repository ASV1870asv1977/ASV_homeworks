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

print('База пользователей.')
user_db = []
while True:
    choice = input('Добавить пользователя в базу => 1\n'
                   'Удалить пользователя из базы => 2\n'
                   'Просмотр базы пользователей  => 3\n'
                   'Выход                        => 4\n'
                   'Введите номер действия: ')
    if choice == '4':
        print(f'{"-" * 50}\nВыход')
        break
    if choice == '1':
        # Ввод данных в базу
        print('-' * 50)
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
        print(f'{"-" * 50}\nНовый пользователь:\n{res}\n{"=" * 50}')
        user_db.append(res)

    if choice == '2':
        # Удаление данных из базы
        if user_db == []:
            print(f'{"-" * 50}\nВ базе нет пользователей.\n{"=" * 50}')
            continue
        number = input(f'{"-" * 50}\nВведите номер удаляемого пользователя: ')
        if number.isalpha() or int(number) < 0 or int(number) >= len(user_db):
            print(f'{"-" * 50}\nВ базе нет пользователя с таким номером!\n{"=" * 50}')
            continue
        else:
            del user_db[int(number)]
            print(f'{"-" * 50}\nПользователь № {number} удален из базы.\n{"=" * 50}')

    if choice == '3':
        # Просмотр базы
        if user_db == []:
            print(f'{"-" * 50}\nВ базе нет пользователей.\n{"=" * 50}')
        print("-" * 50)
        for user in enumerate(user_db):
            print(f'{user[0]}. {user[1]}')
        print("=" * 50)



