"""
Задача № 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве
делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyException(Exception):
    """Класс Моя ошибка"""

    def __init__(self, text):
        """
        Конструктор принимает:
        :param text(str): текст с описанием ошибки
        """
        self.text = text


while True:
    print(f'{"-" * 33}Деление чисел{"-" * 33}')
    user_numbers = input(f'Для выхода введите "q"\n'
                         f'Введите делимое и делитель через пробел: ')
    if 'q' in user_numbers:
        break

    user_numbers = user_numbers.split()

    try:
        if len(user_numbers) != 2:
            raise MyException('Введено неустановленное количество значений')
        for i in range(2):
            if not user_numbers[i].isdigit():
                raise MyException('Введенное значение не является цифрой')
            user_numbers[i] = int(user_numbers[i])
        if user_numbers[1] == 0:
            raise MyException('Деление на ноль запрещено')

    except MyException as e:
        print(e)
        continue

    print(f'Частное равно: {user_numbers[0] / user_numbers[1]}')
