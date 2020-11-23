"""
Задача № 3.   Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).Данные методы должны применяться
только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление
клеток, соответственно. В методе деления должно осуществляться округление значения до целого числа.
"""


from math import ceil


class OrganicCell:
    """Класс Органическая клетка"""

    def __init__(self, quantity_order):
        """
        Конструктор принимает

        :param quantity_order(tuple): количество клеток и ячеек
        """
        self.quantity = quantity_order[0]
        self.order = quantity_order[1]

    def make_order(self):
        """Метод Формирование клетки
        :return list_order, lin(tuple(list, str): количество клеток  по ячейкам, количество клеток  по ячейкам
        """
        lin = ''
        col = self.quantity
        order_temp = self.order
        lines = ceil(self.quantity / self.order)
        list_order = []

        for i in range(lines):
            if i == lines - 1:
                order_temp = self.quantity - order_temp * (lines - 1)
            lin += '*' * order_temp + '\n'
            list_order.append(order_temp)
            col -= order_temp
        # print(f'{lin}')
        return list_order, lin

    def __add__(self, other):
        """Метод перегружает '+' для сложения клеток

        :return sum_quantity, sum_order(tuple): количество клеток, количество ячеек
        """
        sum_quantity = self.quantity + other.quantity
        sum_order = self.order + other.order
        return sum_quantity, sum_order

    def __sub__(self, other):
        """Метод перегружает '-' для взаимного вычитания клеток

        :return sum_quantity, sum_order(tuple): количество клеток, количество ячеек
        """
        sub_quantity = abs(self.quantity - other.quantity)
        sub_order = abs(self.order - other.order)
        return sub_quantity, sub_order

    def __mul__(self, other):
        """Метод перегружает '*' для взаимного умножения клеток

        :return sum_quantity, sum_order(tuple): количество клеток, количество ячеек
        """
        mul_quantity = self.quantity * other.quantity
        mul_order = self.order * other.order
        return mul_quantity, mul_order

    def __truediv__(self, other):
        """Метод перегружает '*' для взаимного деления клеток

        :return sum_quantity, sum_order(tuple): количество клеток, количество ячеек
        """
        truediv_quantity = self.quantity // other.quantity
        if truediv_quantity == 0:
            truediv_quantity = 1
        truediv_order = self.order // other.order
        if truediv_order == 0:
            truediv_order = 1
        return truediv_quantity, truediv_order


def show_cell(cell_1, cell_2, cell_3, number):
    """
    Функция визуализации процессов

    :param cell_1(tuple): экземпляр класса OrganicCell
    :param cell_2(tuple): экземпляр класса OrganicCell
    :param cell_3(tuple): экземпляр класса OrganicCell
    :param number(int): контрольное значение
    """
    cell_list = [cell_1[1], cell_2[1], cell_3[1]]
    for i in range(len(cell_list)):
        cell_list[i] = cell_list[i].split('\n')
        del cell_list[i][-1]
        if len(cell_list[i][-1]) < len(cell_list[i][0]):
            cell_list[i][-1] += (' ' * (len(cell_list[i][0]) - len(cell_list[i][-1])))

    max_lin = max(len(cell_list[0]), len(cell_list[1]), len(cell_list[2]))
    for cell in cell_list:
        for i in range(max_lin):
            if i > len(cell) - 1:
                cell.append(' ' * len(cell[0]))

    for i in range(max_lin):
        if number == 1: sign1 = ' + '
        if number == 2: sign1 = '>-<'
        if number == 3: sign1 = ' * '
        if number == 4: sign1 = '>/<'
        if i == 0:
            print(f'{cell_list[0][i]} {sign1} {cell_list[1][i]}  =  {cell_list[2][i]}')
            continue
        print(f'{cell_list[0][i]}     {cell_list[1][i]}     {cell_list[2][i]}')


while True:
    print(f'{"=" * 80}\nДля выхода введите "q"')
    cell_1 = input('Введите через пробел количество клеток и ячеек 1-го организма: ').split()
    cell_2 = input('Введите через пробел количество клеток и ячеек 2-го организма: ').split()
    if 'q' in cell_1 or 'q' in cell_2:
        break
    if len(cell_1) != 2 or len(cell_2) != 2:
        print('Не введены установленные значения')
        continue

    try:
        for i in range(2):
            cell_1[i] = int(cell_1[i])
            cell_2[i] = int(cell_2[i])
    except ValueError:
        print('Не введены установленные значения')
        continue

    cell_1 = OrganicCell(tuple(cell_1))
    cell_2 = OrganicCell(tuple(cell_2))

    while True:
        number = input(f'{"=" * 80}\n'
                       f'Сложение                 => 1\n'
                       f'Вычитание                => 2\n'
                       f'Умножение                => 3\n'
                       f'Деление                  => 4\n'
                       f'Вод новых организмов     => "q"\n'
                       f'Введите номер задачи: ')
        if number == 'q':
            break
        number = int(number)
        if number == 1:
            cell_3 = cell_1 + cell_2
            print(f'Озганизм № 1:\n{cell_1.make_order()}\n'
                  f'слложить с организмом № 2:\n{cell_2.make_order()}\n'
                  f'получится организм № 3:\n'
                  f'{OrganicCell(cell_3).make_order()}')

        if number == 2:
            cell_3 = cell_1 - cell_2
            if 0 in cell_3:
                print('Вычитание невозможно. Поменяйте параметры организмов!')
                break
            print(f'Взаимное вычитание\n'
                  f'Озганизма № 1:\n{cell_1.make_order()}\n'
                  f'Организма № 2:\n{cell_2.make_order()}\n'
                  f'получится организм № 3:\n'
                  f'{OrganicCell(cell_3).make_order()}')

        if number == 3:
            cell_3 = cell_1 * cell_2
            print(f'Озганизм № 1:\n{cell_1.make_order()}\n'
                  f'умножить на организм № 2:\n{cell_2.make_order()}\n'
                  f'получится организм № 3:\n'
                  f'{OrganicCell(cell_3).make_order()}')

        if number == 4:
            cell_3 = cell_1 / cell_2
            print(f'Озганизм № 1:\n{cell_1.make_order()}\n'
                  f'разделить на организм № 2:\n{cell_2.make_order()}\n'
                  f'получится организм № 3:\n'
                  f'{OrganicCell(cell_3).make_order()}')

        print('-' * 80)
        show_cell(cell_1.make_order(), cell_2.make_order(), OrganicCell(cell_3).make_order(), number)
