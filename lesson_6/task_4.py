"""
Задача № 4.  Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar,
WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость
автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60
(TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""

import pickle, keyboard
from time import sleep


class Car:
    """Класс Car описывает характеристики и действия автомобиля"""

    def __init__(self, speed, color, name, is_police=False):
        """
        Конструктор принимает:

        :param speed(int): сскорость
        :param color(str): цвет
        :param name(str): марка
        :param is_police(bool): является ли полицейской
        """
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        """Метод сообщает, что машина поехала"""
        print(f'Машина {self.color} {self.name} поехала')
        sleep(1)

    def stop(self):
        """Метод сообщает, что машина остановилась"""
        print(f'Машина {self.color} {self.name} остановилась')
        sleep(1)

    def turn(self, direction):
        """Метод сообщает, что машина повернула"""
        print(f'Машина {self.color} {self.name} повернула на {direction}')
        sleep(1)

    def show_speed(self):
        """Метод сообщает скорость автомобиля"""
        print(f'{self.color} {self.name} Ваша скорость {self.speed} км/ч')
        if self.is_police:
            print('Не ограничивайте себя ни в чем')
        sleep(1)

    def police_many(self):
        """Метод сообщает о штрафе"""
        print(f'Вы оштрафованы за превышение скорости')


class TownCar(Car):
    """Класс Городской автомобиль"""

    def show_speed(self):
        """Метод переопределяет Car.show_speed"""
        Car.show_speed(self)
        if self.speed > 60:
            print(f'Вы привысили скорость на {self.speed - 60} км/ч')
            Car.police_many(self)


class SportCar(Car):
    """Класс Спортивный автомобиль"""
    pass


class WorkCar(Car):
    """Класс Грузовик"""

    def show_speed(self):
        """Метод переопределяет Car.show_speed"""
        Car.show_speed(self)
        if self.speed > 40:
            print(f'Вы привысили скорость на {self.speed - 40} км/ч')
            Car.police_many(self)


class PoliceCar(Car):
    """Класс Полицейский автомобиль"""

    def show_speed(self):
        """Метод переопределяет Car.show_speed"""
        Car.show_speed(self)
        if self.speed > 110:
            print(f'Вы привысили скорость на {self.speed - 110} км/ч\n'
                  f'впрочем какая разница Вам можно')


if __name__ == '__main__':
    with open('task_4_cars.pic', 'rb') as f:
        cars_list = pickle.load(f)
        print(cars_list)
    while True:
        print('-' * 50)
        for i in range(len(cars_list)):
            if cars_list[i].is_police:
                cars_list[i].is_police = 'полицейский'
            else:
                cars_list[i].is_police = ''

            print(f'{i}. {cars_list[i].name}, цвет {cars_list[i].color}, '
                  f'скорость {cars_list[i].speed} км/ч, {cars_list[i].is_police}')

        num = input(f'{"-" * 50}\nДля выхода введите "q"\nВведите порядковый номер автомобиля: ')
        if num == 'q': break
        num = int(num)
        print(f'Ваш автомобиль - {cars_list[num].name}\n{"-" * 50}')
        print(f'Начать движение    - "w"\n'
              f'Остановиться       - "s"\n'
              f'Поворот <-         - "a"\n'
              f'Поворот ->         - "d"\n'
              f'Проверить скорость - "g"\n'
              f'Бросить все и уйти - "q"\n'
              f'{"-" * 50}')

        while True:
            if keyboard.is_pressed('q'):
                print('Вы вышли из машины')
                break
            if keyboard.is_pressed('w'):
                cars_list[num].go()
            if keyboard.is_pressed('s'):
                cars_list[num].stop()
            if keyboard.is_pressed('a'):
                cars_list[num].turn('лево')
            if keyboard.is_pressed('d'):
                cars_list[num].turn('право')
            if keyboard.is_pressed('g'):
                cars_list[num].show_speed()
