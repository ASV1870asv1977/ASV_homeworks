"""
Задача № 2.   Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы
для основных классов проекта, проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Сlothes(ABC):
    """Класс Одежда"""

    @abstractmethod
    def __init__(self, name):
        """
        Абстрактный метод Конструктор принимает

        :param name(str): название одежды
        """
        self.name = name

    @abstractmethod
    def consumption(self):
        """Абстрактный метод для расчета расхода ткани"""
        pass


class Coat(Сlothes):
    """Класс Пальто"""

    def __init__(self, name, size, quantity):
        """
        Конструктор принимает

        :param name(str): название одежды
        :param size(str): размер
        :param quantity(int): количество экземпляров
        """
        super().__init__(name)
        self.size = size
        self.quantity = quantity

    @property
    def consumption(self):
        """
        Метод для расчета расхода ткани

        :return: расход ткани
        """
        cons_suit = (float(self.size) / 6.5 + 0.5) * self.quantity
        print(f'{"-" * 80}\n'
              f'Для пошива {self.quantity} экземпляров одежды {self.name} '
              f'расход ткани составил {cons_suit}')
        return cons_suit


class Suit(Сlothes):
    """Класс Костюм"""

    def __init__(self, name, growth, quantity):
        """
        Конструктор принимает

        :param name(str): название одежды
        :param size(str): рост
        :param quantity(int): количество экземпляров
        """
        super().__init__(name)
        self.growth = growth
        self.quantity = quantity

    @property
    def consumption(self):
        """
        Метод для расчета расхода ткани

        :return: расход ткани
        """
        cons_suit = (2 * float(self.growth) + 0.3) * quantity
        print(f'{"-" * 80}\n'
              f'Для пошива {self.quantity} экземпляров одежды {self.name} '
              f'расход ткани составил {cons_suit}')
        return cons_suit


def show_consumption(consum):
    """Функция определения общего расхода ткани

    :param consum(dict): расход ткани по видам одежды
    """
    sum_val = 0
    for val in consum.values():
        sum_val += sum(val)

    print(f'Общий расход ткани: {sum_val}')


consum = {'пальто': [], 'костюм': []}
while True:
    number = input(f'{"=" * 80}\n'
                   f'Для выхода введите "q"\n'
                   f'Пальто      => 1\n'
                   f'Костюм      => 2\n'
                   f'Введите номер типа одежды для пошива: ')
    if number == 'q':
        break
    quantity = int(input('Введите количество экземпляров для пошива: '))

    if number == '1':
        size = input('Введите размер: ')
        el = Coat('пальто', size, quantity)
        consum[el.name].append(el.consumption)

    elif number == '2':
        growth = input('Введите рост: ')
        el = Suit('костюм', growth, quantity)
        consum[el.name].append(el.consumption)

    show_consumption(consum)
