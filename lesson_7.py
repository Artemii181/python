# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы.Подсказка: матрица — система некоторых математических
# величин, расположенных в виде прямоугольной схемы.Примеры матриц вы найдете в методичке.Следующий шаг — реализовать
# перегрузку метода __str__() для вывода матрицы в привычном виде.Далее реализовать перегрузку метода __add__() для
# реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая
# матрица.Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, input_text):
        self.input = input_text

    def __str__(self):
        return '\n'.join([' '.join([str(el) for el in line]) for line in self.input])

    def __add__(self, other):
        answer = ''
        if len(self.input) == len(other.input):
            for line_1, line_2 in zip(self.input, other.input):
                if len(line_1) != len(line_2):
                    return 'Проблема с формой'

                sum_line = [x + y for x, y in zip(line_1, line_2)]
                answer += ' '.join([str(i) for i in sum_line]) + '\n'
            else:
                return answer




matrix_1 = Matrix([[1, 2], [3, 4], [5, 6], [7, 8]])
matrix_2 = Matrix([[3, 4], [5, 6], [7, 8], [9, 10]])

print(matrix_1)
print()
print(matrix_1 + matrix_2)


#2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
# проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные
# числа: V и H, соответственно.Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
# (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.Реализовать общий подсчет
# расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных
# классов проекта, проверить на практике работу декоратора @property.


from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, para):
        self.para = para

    @abstractmethod
    def calculate(self):
        pass

class Coat(Clothes):

    @property
    def calculate(self):
        return round((self.para / 6.5) + 0.5)

class Suit(Clothes):

    @property
    def calculate(self):
        return round((2 * self.para) + 0.3)

coat = Coat(45)
suit = Suit(170)
print(coat.calculate)
print(suit.calculate)

#3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе
# инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы
# методы перегрузки арифметических операторов:
# сложение (__add__()),
# вычитание (__sub__()),
# умножение (__mul__()),
# деление (__truediv__())


class Cell:
    def __init__(self, nums):
        self.nums = nums

    def my_funk(self, el):
        return '\n'.join(['*' * el for _ in range(self.nums // el)]) + '\n' + '*' * (self.nums % el)

    def __str__(self):
        return str(self.nums)

    def __add__(self, other):
        return 'Сумма ячеек равна ' + str(self.nums + other.nums)

    def __sub__(self, other):
        return self.nums - other.nums if self.nums - other.nums > 0 \
            else 'Ячеек в первой клетке меньше или равно второй, вычитание не возможно'

    def __mul__(self, other):
        return 'Умножение клеток ' + str(self.nums * other.nums)

    def __truediv__(self, other):
        return 'Истинное деление ячеек' + str(round(self.nums / other.nums))

cell1 = Cell(10)
cell2 = Cell(34)
print(cell1)
print(cell1 + cell2)
print(cell2.my_funk(9))