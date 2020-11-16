"""
Задача № 1.  Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""

import os

flag = 0

# Отработка действий в соответствии с контекстным меню
while True:
    number = input(f'{"=" * 50}\n'
                   f'Записать файл     => 1\n'
                   f'Читать файл       => 2\n'
                   f'Выход             => 3\n'
                   f'Введите номер задачи: ')
    # Запись в файл
    if number == '1':
        flag = 1
        with open('task_1.txt', 'w', encoding='utf-8') as f:
            user_list = []
            while True:
                user_text = input('Введите текст: ')
                user_list.append(f'{user_text}\n')
                if not user_text:
                    break

            f.writelines(user_list)
            print(f'{"-" * 50}\nФайл {f.name} записан')

    # Чтение из файла
    if number == '2':
        if flag == 1:
        #if 'task_1.txt' in os.listdir('data_files'):
            with open('task_1.txt', 'r', encoding='utf-8') as f:
                print(f'{"-" * 50}\nФайл {f.name}:')
                print(f.read())
        else:
            print(f'{"-" * 50}\nЧитаемый файл отсутствует в директории')

    if number == '3':
        print(f'{"-" * 50}\nВыход')
        break
