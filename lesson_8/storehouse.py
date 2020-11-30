# ----------------------------------------------------------------------------------------------------------------------
# Program by Sergey A.
# LogisticsStoreHouse
#
# Version           Data               Info
#  1.1             2020/30        Initial Version
# ______________________________________________________________________________________________________________________
"""
Размещение классов и функций
"""


from tkinter import *
from tkinter.ttk import Combobox
import datetime

class Storehouse:
    """Класс Склад"""

    def __init__(self, quantity, surname, rack_number=None, vendor_code=None):
        """
        Конструктор принимает:
        :param rack_number(int): стелажный номер
        :param vendor_code(int): артикул
        :param quantity(int): количество на складе
        :param surname(str): фамилия кладовщика
        """
        self.rack_number = rack_number
        self.vendor_code = vendor_code
        self.surname = surname
        self.quantity = quantity

    @classmethod
    def arrival(cls, quantity, mov_counter):
        """
        Метод класса Склад отвечающий за изменение суммы оргтехники
        :param quantity_in(int): количество
        :return:
        """
        if not mov_counter:
            quantity = -quantity
        return quantity


    @staticmethod
    def numbers_valid(str_data, real_data):
        """
        Статический метод проверяет соответствие принятой даты реальным значениям
        :param seq_data (str): строка с числовыми значением года
        :param real_data (int): значение текущего года года
        :return (bool):bool-значение по установленным параметрам
        """
        try:
            year = int(str_data)
        except ValueError:
            return
        return 2000 < year <= real_data

    def changes(self, chang):
        """Метод осуществляющий изменения наличия оргтехники на складе на складе"""
        self.quantity = self.quantity + chang

    @staticmethod
    def quantity_valid(str_number):
        """
        Статический метод проверяет соответствие указанного количества техники
        :param str_number(str): строка с числовыми значением количества техники
        :return (bool):bool-значение по установленным параметрам
        """
        try:
            quantity = int(str_number)
        except ValueError:
            return
        return quantity > 0

    def changes(self, chang):
        """Метод осуществляющий изменения наличия оргтехники на складе на складе"""
        self.quantity = self.quantity + chang


class Equipment(Storehouse):
    """Класс Оргтехника"""

    def __init__(self, manufacturer, year, rack_number=None, vendor_code=None):
        self.manufacturer = manufacturer
        self.year = year
        super().__init__(rack_number, vendor_code)


class Computer(Equipment):
    """Класс Компьтер"""

    def __init__(self, cpu, os, manufacturer, year=None, rack_number=None, vendor_code=None):
        self.cpu = cpu
        self.os = os
        super().__init__(manufacturer, year, rack_number, vendor_code)


class Monitor(Equipment):
    """Класс Монитор"""
    def __init__(self, model, diagonal, manufacturer, year=None, rack_number=None, vendor_code=None):
        self.model = model
        self.diagonal = diagonal
        super().__init__(manufacturer, year, rack_number, vendor_code)


class Printer(Equipment):
    """Класс Принтер"""
    def __init__(self, model, color, manufacturer, year=None, rack_number=None, vendor_code=None):
        self.model = model
        self.color = color
        super().__init__(manufacturer, year, rack_number, vendor_code)


if __name__ == '__main__':

    a_1 = 1
    a_4 = 'Jones'

    """
    product = Storehouse(a_1, a_4)
    print(product.quantity, product.vendor_code, product.surname)

    prod_chang = Storehouse.arrival('NIISSU', 10)
    print(prod_chang)
    product.changes(prod_chang[1])
    print(product.quantity, product.vendor_code, product.surname)

    prod_chang = Storehouse.delivery('RTI', 16)
    print(prod_chang)
    product.changes(prod_chang[1])
    print(product.quantity, product.vendor_code, product.surname)

    comp = Equipment('HP', 2019, 'H-2134E', a_1, a_4)
    print(comp.vendor_code, comp.manufacturer, comp.year, comp.quantity, comp.rack_number)
    """
    b = Computer('i7', 'Acer', 2018, 10, 'Smith',)
    print(b.rack_number, b.cpu, b.quantity, b.vendor_code, b.manufacturer, b.year)




