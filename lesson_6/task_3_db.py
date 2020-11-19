# ---------------------------------------------------------------------------
# Program by Sergey A.
#
#
# Version           Data               Info
#  1.0             2020/11        Initial Version
# ___________________________________________________________________________

"""
Программа 'База данных сотрудников фирмы' позволяет добавлять сотрудников в базу данных,
удалять из базы, просматривать базу. Сохраняет данные в pickle-формате в файле employees.pic.
Классы и функции, применяемые в программе расположены в модуле employees.py.
"""

import pickle, employees

attr_worker_list = ['имя', 'фамилию', 'должность', 'оклад', 'премию']
with open('employees.pic', 'rb') as f:
    workers_db = pickle.load(f)

while True:
    choice = input('Добавить сотрудника в базу => 1\n'
                   'Удалить сотрудника из базы => 2\n'
                   'Просмотр базы сотрудников  => 3\n'
                   'Выход                      => 4\n'
                   'Введите номер действия: ')
    if choice == '4':
        print(f'{"-" * 50}\nВыход')
        break

    if choice == '1':
        # Ввод данных в базу
        print('-' * 50)
        worker_list = []

        for i in range(5):
            worker_list.append(input(f'Введите {attr_worker_list[i]} сотрудника: '))
        try:
            worker_list[3] = int(worker_list[3])
            worker_list[4] = int(worker_list[4])
        except ValueError:
            print('Ошибка ввода данных!')
            worker_list = []
            continue

        worker = employees.Position(worker_list[0], worker_list[1], worker_list[2], worker_list[3], worker_list[4])
        workers_db.append(worker)
        print(f'Запись проведена\n{"=" * 50}')

        with open('employees.pic', 'wb') as f:
            pickle.dump(workers_db, f)

    if choice == '3':
        # Просмотр базы
        with open('employees.pic', 'rb') as f:
            workers_db = pickle.load(f)

        employees.show_empl(workers_db)
        print('=' * 50)

    if choice == '2':
        # Удаление данных из базы
        with open('employees.pic', 'rb') as f:
            workers_db = pickle.load(f)

        employees.show_empl(workers_db)
        number = input(f'{"-" * 50}\nДля отмены нажмите "q"\nВведите номер удаляемого пользователя: ')
        if number.isalpha() or int(number) < 0 or int(number) >= len(workers_db):
            print(f'{"-" * 50}\nВ базе нет пользователя с таким номером!\n{"=" * 50}')
            continue
        else:
            del workers_db[int(number)]
            print(f'Пользователь удален\n{"=" * 50}')

        with open('employees.pic', 'wb') as f:
            pickle.dump(workers_db, f)
