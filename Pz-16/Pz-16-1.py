# Создайте класс «Круг», который имеет атрибут радиуса и методы для вычисления
# площади, длины окружности и диаметра.

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

    def diameter(self):
        return 2 * self.radius


circle = Circle(5)

print("Радиус:", circle.radius)
print("Площадь:", circle.area())
print("Длина окружности:", circle.circumference())
print("Диаметр:", circle.diameter())
