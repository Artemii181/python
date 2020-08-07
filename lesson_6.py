#1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном
# порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.

from time import sleep
from itertools import cycle

class TrafficLights :
    def __init__(self):
        self.__color = (('Red', 5), ('Yellow', 2), ('Green', 4))

    def run(self):
        for color, sec in cycle(self.__color):
            print(color, '(wait {} sec)'.format(sec))
            sleep(sec)

traffic_lights = TrafficLights()
traffic_lights.run()

#2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
# атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета
# массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина * ширина * масса
# асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна.
# Проверить работу метода.

class Track:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def sum_mass(self):
        mass = self._width * self._length * 25 * 5 / 1000
        print(mass, 'т')
my_track = Track(20, 5000)
my_track.sum_mass()

#3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
# реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
# атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.income_wage = income['wage']
        self.income_bonus = income['bonus']

class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname, self.position)

    def get_total_income(self):
        print(self.income_wage + self.income_bonus)

pos = Position('Stas', 'Ivanov', 'junior', {"wage": 30000, "bonus": 10000})
pos.get_full_name()
pos.get_total_income()

#4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police
# (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print('{} is going!'.format(self.name))
    def stop(self):
        print('{} is stoping!'.format(self.name))
    def turn(self, direction):
        print('{} is turning to! {}'.format(self.name, direction))
    def my_speed(self):
        print('Current speed:'.format(self.speed))
class TownCar(Car):
    def my_speed(self):
        print('Current speed:', self.speed)
        if self.speed > 60:
            print ('Warning! Your speed is more than max')

class SportCar(Car):
    pass

class WorkCar(Car):
    def my_speed(self):
        print('Current speed:', self.speed)
        if self.speed > 40:
            print ('Warning! Your speed is more than max')

class PoliceCar(Car):
    pass

sport_car = SportCar(300, 'Ярко красная', 'Спортивная машина', False)
town_car = TownCar(65, 'Белая', 'Городская машина', False)
work_car = WorkCar(45, 'Серая', 'Рабочая машина', False)
police_car = PoliceCar(250, 'Черная', 'Полицейская машина', True)

sport_car.my_speed()
town_car.my_speed()
work_car.my_speed()
police_car.my_speed()
sport_car.turn('left')

#5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
# (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
# Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен
# выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого
# экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def my_funk(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def my_funk(self):
        print('Ручка рисует')

class Pencil(Stationery):
    def my_funk(self):
        print('Карандаш рисует')

class Handle(Stationery):
    def my_funk(self):
        print('Маркер рисует')

pen = Pen('ручка')
pencil = Pencil('карандаш')
handle = Handle('маркер')

pen.my_funk()
pencil.my_funk()
handle.my_funk()