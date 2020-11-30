"""
Задача № 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной
структуры на реальных данных.
"""


class Data:
    """Класс Data """

    def __init__(self, data):
        """
        Конструктор принимает:
        :param data(str):  дата в формате дд-мм-гггг
        """
        self.data = data

    @classmethod
    def numbers(cls, str_data):
        """
        Метод класса преобразует строку с датой в численные значения
        :param str_data(str): дата в формате дд-мм-гггг
        :return (tuple(int)): кортеж с числовыми значениями даты
        """
        day, month, year = map(int, str_data.split('-'))
        return day, month, year

    @staticmethod
    def numbers_valid(seq_data):
        """
        Статический метод проверяет соответствие принятой даты реальным значениям
        :param seq_data (list(tuple)(int)): кортеж (список) с числовыми значениями даты
        :return (tuple(bool)): кортеж с bool-значениями по установленным параметрам
        """
        day, month, year = map(int, seq_data)
        return 0 < day <= 31, 0 < month <= 12, 0 < year <= 6000


class MyException(Exception):
    """Класс Моя ошибка"""
    def __init__(self, text):
        """
        Конструктор принимает:
        :param text(str): текст с описанием ошибки
        """
        self.text = text


while True:
    user_data = input(f'{"-" * 80}\nДля выхода введите "q"\nВведите дату в формате дд-мм-гггг: ')
    if 'q' in user_data:
        break
    if '-' in user_data:
        pass
    else:
        print('Неустановленный формат')
        continue

    user_data = user_data.split('-')

    try:
        if len(user_data) != 3:
            raise MyException('Неустановленный формат')

        for i in range(3):
            if not user_data[i].isdigit():
                raise MyException('Введенное значение не является цифрой')
            elif len(user_data[i]) != 2 and i == 0:
                raise MyException('Введено значение числа неустановленной длины')
            elif len(user_data[i]) != 2 and i == 1:
                raise MyException('Введено значение месяца неустановленной длины')
            elif len(user_data[i]) != 4 and i == 2:
                raise MyException('Введено значение года неустановленной длины')

        bool_data = Data.numbers_valid(user_data)
        if False in bool_data:
            raise MyException('Неустановленное значение даты')

    except MyException as e:
        print(e)
        continue

    user_data = '-'.join(user_data)

    # Экземпляр класса Data возвращает принятую строку
    d = Data(user_data)
    print(f'{d.data} - принятая строка')

    # Метод класса возвращает кортеж с числовыми значениями даты
    a = Data.numbers(user_data)
    print(f'{a} - кортеж с числовыми значениями даты')

    # Статический метод возвращает кортеж с bool-значениями по установленным параметрам
    print(f'{Data.numbers_valid(a)} - кортеж с bool-значениями по установленным параметрам')
