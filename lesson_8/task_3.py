"""
Задача № 3. Создайте собственный класс-исключение, который должен проверять содержимое списка
на наличие только чисел. Проверить работу исключения на реальном примере. Необходимо запрашивать
у пользователя данные и заполнять список. Класс-исключение должен контролировать типы данных
элементов списка.
"""


class MyException(Exception):
    """Класс Моя ошибка"""

    def __init__(self, text):
        """
        Конструктор принимает:
        :param text(str): текст с описанием ошибки
        """
        self.text = text

    def str_Exception(self):
        """Метод определения чисел"""
        if not self.text.isdigit():
            print('Введенные данные не являются цифрами')
            return False
        return int(self.text)


user_numbers = []
while True:
    print(f'{"-" * 33}Список чисел{"-" * 33}')
    user_text = input(f'Для выхода введите "q"\n'
                      f'Для вывода числовых значений введите "w"\n'
                      f'Введите данные: ')
    if user_text == 'q':
        print(user_numbers)
        break
    if user_text == 'w':
        print(user_numbers)
        continue

    user_data = MyException(user_text)
    if user_data.str_Exception():
        user_numbers.append(user_data.str_Exception())
