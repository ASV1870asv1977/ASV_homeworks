"""
Модуль с классами и фкнкциями для программы 'База данных сотрудников фирмы'
"""


class Worker:
    """Класс Worker(Рабочий)"""

    def __init__(self, name, surname, position, wage, bonus):
        """
        Конструктор принимает
        :param name (str): имя
        :param surname (str): фамилия
        :param position (str): должность
        :param wage (int): оклад
        :param bonus (int): премия
        """
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    """
    Класс Position (Должность) наследует атрибуты класса Worker
    """

    def get_full_name(self):
        """Метод для вывода имени, фамилии, должности"""

        print(self.name, self.surname, self.position)

    def get_total_income(self):
        """Метод для вывода полного дохода"""

        print(self._income['wage'] + self._income['bonus'])


def show_empl(workers_db):
    print('-' * 50)
    for i in range(len(workers_db)):
        print(i, end='. ')
        workers_db[i].get_full_name()
        print('   Доход: ', end='')
        workers_db[i].get_total_income()


if __name__ == '__main__':
    a = Position('Bob', 'Smith', 'manager', 50000, 5000)
    a.get_full_name()
    a.get_total_income()
    workers_db = [a]
    show_empl(workers_db)