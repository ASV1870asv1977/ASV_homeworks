"""
Задача № 3.  Реализовать базовый класс Worker (работник), в котором определить
атрибуты: name, surname, position (должность), income (доход). Последний атрибут должен быть
защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
{"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать
 методы экземпляров).
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
    Класс Position (Должность) наследующет атрибуты класса Worker
    """

    def get_full_name(self):
        """Метод для вывода имени и фамилии"""

        print(self.name, self.surname)

    def get_total_income(self):
        """Метод для вывода полного дохода"""

        print(self._income['wage'] + self._income['bonus'])


if __name__ == '__main__':
    a = Position('Bob', 'Smith', 'manager', 50000, 5000)
    b = Position('Kate', 'Jones', 'developer', 55000, 7000)
    a.get_full_name()
    a.get_total_income()
    b.get_full_name()
    b.get_total_income()


