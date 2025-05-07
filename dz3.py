from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def info(self):
        pass

class Square(Shape):
    def __init__(self, side, color):
        self.side = side
        self.color = color

    @property
    def perimeter(self):
        return self.side * 4

    @property
    def area(self):
        return self.side ** 2

    def draw(self):
        for _ in range(self.side):
            print("*" * self.side)

    def info(self):
        print(f"===Квадрат===")
        print(f"Сторона: {self.side}")
        print(f"Цвет: {self.color}")
        print(f"Площадь: {self.area}")
        print(f"Периметр: {self.perimeter}")

class Rectangle(Shape):
    def __init__(self, length, width, color):
        self.length = length
        self.width = width
        self.color = color

    @property
    def perimeter(self):
        return 2 * (self.length + self.width)

    @property
    def area(self):
        return self.length * self.width

    def draw(self):
        for _ in range(self.length):
            print("*" * self.width)

    def info(self):
        print(f"===Прямоугольник===")
        print(f"Длина: {self.length}")
        print(f"Ширина: {self.width}")
        print(f"Цвет: {self.color}")
        print(f"Площадь: {self.area}")
        print(f"Периметр: {self.perimeter}")

class Triangle(Shape):
    def __init__(self, side1, side2, side3, color):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.color = color

    @property
    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    @property
    def area(self):
        s = self.perimeter / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def draw(self):
        for i in range(1, self.side1 + 1):
            print(" " * (self.side1 - i) + "*" * (2 * i - 1))

    def info(self):
        print(f"===Треугольник===")
        print(f"Сторона 1: {self.side1}")
        print(f"Сторона 2: {self.side2}")
        print(f"Сторона 3: {self.side3}")
        print(f"Цвет: {self.color}")
        print(f"Площадь: {self.area:.2f}")
        print(f"Периметр: {self.perimeter}")

# Примеры использования
square = Square(3, "red")
square.info()
square.draw()

rectangle = Rectangle(3, 7, "green")
rectangle.info()
rectangle.draw()

triangle = Triangle(6, 6, 11, "blue")
triangle.info()
triangle.draw()