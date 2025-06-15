# from abc import ABC, abstractmethod
# import math
#
# class Shape(ABC):
#     @abstractmethod
#     def perimeter(self):
#         pass
#
#     @abstractmethod
#     def area(self):
#         pass
#
#     @abstractmethod
#     def draw(self):
#         pass
#
#     @abstractmethod
#     def info(self):
#         pass
#
# class Square(Shape):
#     def __init__(self, side, color):
#         self.side = side
#         self.color = color
#
#     @property
#     def perimeter(self):
#         return self.side * 4
#
#     @property
#     def area(self):
#         return self.side ** 2
#
#     def draw(self):
#         for _ in range(self.side):
#             print("*" * self.side)
#
#     def info(self):
#         print(f"===Квадрат===")
#         print(f"Сторона: {self.side}")
#         print(f"Цвет: {self.color}")
#         print(f"Площадь: {self.area}")
#         print(f"Периметр: {self.perimeter}")
#
# class Rectangle(Shape):
#     def __init__(self, length, width, color):
#         self.length = length
#         self.width = width
#         self.color = color
#
#     @property
#     def perimeter(self):
#         return 2 * (self.length + self.width)
#
#     @property
#     def area(self):
#         return self.length * self.width
#
#     def draw(self):
#         for _ in range(self.length):
#             print("*" * self.width)
#
#     def info(self):
#         print(f"===Прямоугольник===")
#         print(f"Длина: {self.length}")
#         print(f"Ширина: {self.width}")
#         print(f"Цвет: {self.color}")
#         print(f"Площадь: {self.area}")
#         print(f"Периметр: {self.perimeter}")
#
# class Triangle(Shape):
#     def __init__(self, side1, side2, side3, color):
#         self.side1 = side1
#         self.side2 = side2
#         self.side3 = side3
#         self.color = color
#
#     @property
#     def perimeter(self):
#         return self.side1 + self.side2 + self.side3
#
#     @property
#     def area(self):
#         s = self.perimeter / 2
#         return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
#
#     def draw(self):
#         for i in range(1, self.side1 + 1):
#             print(" " * (self.side1 - i) + "*" * (2 * i - 1))
#
#     def info(self):
#         print(f"===Треугольник===")
#         print(f"Сторона 1: {self.side1}")
#         print(f"Сторона 2: {self.side2}")
#         print(f"Сторона 3: {self.side3}")
#         print(f"Цвет: {self.color}")
#         print(f"Площадь: {self.area:.2f}")
#         print(f"Периметр: {self.perimeter}")
#
#
# square = Square(3, "red")
# square.info()
# square.draw()
#
# rectangle = Rectangle(3, 7, "green")
# rectangle.info()
# rectangle.draw()
#
# triangle = Triangle(6, 6, 11, "blue")
# triangle.info()
# triangle.draw()

#
# squares = map (lambda x: x *x ,[0,1,2,3,4])
# print(list(squares))

# d = {}
# if d:
#     print("Hello, world")
# else:
#     print("It is empty")

# x = 23
# num = 0 if x > 10 else 11
# print(num)

# for i in "hello world":
#     if i == "o":
#         break
#     print(i *2 , end = "")
# a = set ("hello")
#
# print(len(a))

# another_dict = {'a':{'a':['a']}}
# print(another_dict.pop('a')== another_dict.clear())

# e = lambda x : x
# a = {1,2,3}
# b = e (a)
# print(a==b)

# while 1:
#     print(1, break)

# d = [1,1,2]
# print(len(set(d)))

# for i in range(5):
#     if i % 2 == 0:
#         continue
#     print(i)

# a = int ("qwerty")
# print(a)

# tuple_1 = (1,2,3)
# tuple_2 = (4,5,6)
# tuple_3= tuple_1+ tuple_2
#
# print(tuple_1< tuple_2)
# print(tuple_2<tuple_3)
# print(tuple_1<tuple_3)

# c = type({1:2,2:1}) == type ({1,2})
#
# print(c)

# import random
# print(random.uniform(1,1.1))

# a -= 1
# print(a)

# for i in range(1):
#     print(i)

# try:
#     print(1)
# except Exception:
#     print(0)
#
# e = "string"
# print(e[-3:6])

# b = "python"
# print(b[:6:2])
# b = lambda x , y:print(y)
#
# b(1,2)

# for i in "str":
#     print(i.upper(),end=".")
# a = {"a":10,"c":30}
# b = {"c":20,"e":5}
# for i in a.keys():
#     if i not in b:
#         b[i]= a[i]
# print(b)
#
# import random
# print(random.random())

# c = id ([1])== id ([1.0])
# print(c)


# try:
#     a = 2 + "1"
#     print(a)
# except TypeError:
#     print("Error")

# e = [1]+"1"
# print(e)

# e = id ({1}) == id ({1})
# print(e)


# import random
# print(2.1==random.uniform(2.1,2.1))

# a = [1]+[1]
# print(a)

# old_dict = {"a": 10 ,"b":10}
# new_dict = {}
#
# for i , j in old_dict.items():
#     new_dict[j]= i
#     print(new_dict)
# proghubPython = True
# def fun1():
#     proghubPython = None
#
#     def fun2():
#         global proghubPython
#         proghubPython = "py"
#     fun2()
#
# fun1()
# print(proghubPython)

# c = frozenset([1,2,3]) == {1,2,3}
# print(c)

# d = " some string"
#
# d[5:12] = "int"
#
# print(d)

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return  n * factorial(n-1)
#
# print(factorial(5))

# proghubPython = True
# def fun1():
#     global proghubPython
#     proghubPython= None
#
#     def fun2():
#
#         proghubPython = "py"
#     fun2()
#
# fun1()
# print(proghubPython)

# c = "some str "
# print(c[-3:9]+" "+c[0:5])

# for  i in range(len("str")):
#     if i !=2:
#         print("str"[i], end = "-")
#     else:
#         print("str"[1])


# c= "str"
# print(c[0:3])

# a = 1
# for i in range(5):
#     a = a * i
# print(a)


# b = [1,2,3]+ []
#
# print(b)

# n = 2.8956
#
# print(f"{n:2f}")


# a = [1, 2] - 1
# print(a)

# a = lambda  x: x +x
# print(a(2))

# c = [1,2]+[0]
# print(c)


# dict={{{"Socrat": "Empty"}:{'Plato':"A lot of material"}}:"again"}
# key = {'Socrat:'"Empty"}
# print(dict[key]["Plato"])

# b = lambda :print("str")
#
# type (b())

# d = {1,2} == set ([1,2])
# print(d)

# c = lambda x: print(0)
# c(5)

# d = lambda : False
# print(d())


for i in range(-2):
    print(i )
