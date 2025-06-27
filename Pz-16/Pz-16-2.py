# Создайте класс "Фигура", который содержит метод расчета площади фигуры.
# Создайте классы "Квадрат" и "Прямоугольник", которые наследуются от класса
# "Фигура". Каждый класс должен иметь метод расчета площади собственной фигуры.

# Базовый класс
class Figure:
    def area(self):
        raise NotImplementedError("Метод area() должен быть переопределён в подклассе")


# Класс Квадрат
class Square(Figure):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


# Класс Прямоугольник
class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


square = Square(4)
rectangle = Rectangle(5, 3)

print("Площадь квадрата:", square.area())
print("Площадь прямоугольника:", rectangle.area())