"""
Задача № 1.  Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
"""


class Matrix:
    """Класс Матрица"""

    def __init__(self, matr):
        """
        Конструктор принимает двумерную матрицу

        :param matr(list): список списков
        """

        self.matr = matr

    def __str__(self):
        """Метод перегружает print() для вывода матрицы в привычном виде

        :return (str): список списков построчно
        """

        return f'Матрица:\n{self.matr[0]}\n{self.matr[1]}'

    def __add__(self, other):
        """Метод перегружает '+' для сложения матриц

        :return sum_matr(list): список списков
        """

        sum_matr = []
        for i in range(len(self.matr)):
            matr_list = []
            for (a, b) in zip(self.matr[i], other.matr[i]):
                matr_list.append(a + b)
            sum_matr.append(matr_list)

        return sum_matr


matr_1 = Matrix([[1, 2, 3], [4, 5, 6]])
print(matr_1)
matr_2 = Matrix([[2, 3, 4], [5, 6, 1]])
print(matr_2)
matr_3 = matr_1 + matr_2
print(Matrix(matr_3))
