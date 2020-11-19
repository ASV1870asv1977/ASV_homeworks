"""
Задача № 2.  Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
"""


class Road:
    """Класс Дорога."""

    def __init__(self, length, width):
        """
        Конструктор принимает:

        :param length:
        :param width:
        """
        self._length = length
        self._width = width

    def calc_mass(self):
        """
        Метод для вычисления массы асфальта

        :return (float): масса асфальта
        """
        while True:
            height = input('Введите толщину дорожного полотна, см: ')
            try:
                height = int(height)
                break
            except ValueError:
                print(f'Проверте правильность ввода данных\n{"-" * 50}')
                continue
        mass_const = 25
        return round(self._length * self._width * mass_const * height / 1000, 3)


while True:
    print('Для выхода введите "q"')
    size = input('Введите длинну дороги и ширину дороги в метрах через пробел: ').split()
    if 'q' in size:
        break
    if len(size) != 2 or not size[0].isdigit() or not size[1].isdigit():
        print(f'Проверте правильность ввода данных\n{"=" * 50}')
        continue

    my_way = Road(int(size[0]), int(size[1]))
    print(f'{"-" * 50}\n'
          f'Масса асфальта для обустройства дороги: {my_way.calc_mass()} т\n'
          f'{"=" * 50}')
