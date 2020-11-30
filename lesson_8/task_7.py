"""
Задача № 7.   Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав
экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров. Проверьте
корректность полученного результата.
"""


class ComplexNumber:
    """Класс Комплексное число"""

    def __init__(self, number1, number2):
        """
        Конструктор принимает
        :param number1(int): 1-е действительное число
        :param number(int)2: 2-е действительное число без мнимой единицы
        """
        self.number1 = number1
        self.number2 = number2

    def __add__(self, other):
        """Метод перегружает '+' для сложения комплексных чисел

        :return ComplexNumber(sum_number1, sum_number2)(tuple): объект класса (сумма комплексных чисел)
        """
        sum_number1 = self.number1 + other.number1
        sum_number2 = self.number2 + other.number2
        return ComplexNumber(sum_number1, sum_number2)

    def __mul__(self, other):
        """Метод перегружает '*' для умножения комплексных чисел

        :return comp_number: объект класса
        """
        mul_number1_1 = self.number1 * other.number1
        mul_number1_2 = self.number1 * other.number2
        mul_number2_1 = self.number2 * other.number2 * -1
        mul_number2_2 = self.number2 * other.number1
        comp_number = ComplexNumber(mul_number1_1, mul_number1_2) + ComplexNumber(mul_number2_1, mul_number2_2)
        return comp_number


while True:
    numbers = input(f'Введите два действительных числа комплексного числа через пробел: ').split()
    numb1, numb2 = [int(numbers[0]), int(numbers[1])]
    comp_number1 = ComplexNumber(numb1, numb2)
    print(f'Первое комплексное число: {numb1} {numb2}i')
    numbers = input(f'Введите два действительных числа комплексного числа через пробел: ').split()
    numb1, numb2 = [int(numbers[0]), int(numbers[1])]
    comp_number2 = ComplexNumber(numb1, numb2)
    print(f'Второе комплексное число: {numb1} {numb2}i')

    n = input(f'{"-" * 80}Для выхода нажмите "q"\n'
              f'Сложение           => 1\n'
              f'Умножение          => 2\n'
              f'Выбирите действие: ')

    if n == 'q':
        break

    if n == '1':
        comp_number3 = comp_number1 + comp_number2
        print(f'Сумма комплексных чисел равна: {comp_number3.number1} {comp_number3.number2}i\n{"=" * 80}')

    if n == '2':
        comp_number3 = comp_number1 * comp_number2
        print(f'Произведение комплексных чисел равно: {comp_number3.number1} {comp_number3.number2}i\n{"=" * 80}')



