# name = "admin"
# print("Hello", name)
# age = 20.2
# print(age)
#
# print(type(name))
# print(type(age))
#
# print(id(name))
# print(id(age))

# a = b = c = 10
# a, b, c = 5, "Hello", 7.2
# print(a)
# print(b)
# print(c)

# name = "admin"
# print(name)

# import keyword
# print(keyword.kwlist)

# PI = 3.14
# print(PI)

# a = 5
# print(a)
# a = "Hello"
# print(a)
# a = 1.2
# print(a)

# a = 5
# b = 20
# print("a:", a)
# print("b:", b)
#
# # c = a  # 1
# # a = b  # 2
# # b = c  # 1
#
# print("a:", a)
# print("b:", b)

# print("строка "
#       "символов")
# print('\tстрока \nсимв      олов')

# a = 5
# b = 20
# print("a:", a)
# print("b:", b)
#
# # a = a + b  # 3
# # b = a - b  # 1
# # a = a - b  # 2
#
# a, b = b, a
#
# print("a:", a)
# print("b:", b)

# print("Документ \"file.txt\" находится по пути: \rD:\\\\folder\\file.txt")

# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + ", " + s2 + "!\t\t"  # конкатенация
# print(s3)
# s4 = s3 * 5
# print(s4)

# print(6 + 2)
# print(6.2 + 2.4)
# print(6 - 2)
# print(6 * 2)
# print(7 / 2)
# print(6 / 2)
#
# print(7 // 2)
# print(6 // 2)
#
# print(6 ** 2)
#
# print(7 % 2)

# a = 5
# b = 7
# c = 3
# d = a + b + c
# print(d)
# f = a * b * c
# print(f)
# g = d / 3
# print(g)

# number = (6 + 4) * (5 ** 2 + 7)
# print(number)

# a = 5
#
# a += 3  # a = a + 3
# print(a)  # 8
#
# a -= 3  # a = a - 3
# print(a)  # 5
#
# a *= 4  # a = a * 4
# print(a)  # 20

# num = 9753  # 4
# print("Исходное число:", num)
# a = num % 10
# print("a:", a)
# num = num // 10
# # print(num)
# b = num % 10
# print("b:", b)
# num = num // 10
# # print(num)
# c = num % 10
# print("c:", c)
# num = num // 10
# # print(num)
# d = num % 10
# print("d:", d)
# print("Обратное число:", a * 1000 + b * 100 + c * 10 + d)


# num = 4321  #
# print("Исходное число:", num)
# res = num % 10 * 1000  # 1000
# num //= 10
# res += num % 10 * 100  # 200    res = res + num % 10 * 100
# num //= 10
# res += num % 10 * 10
# num //= 10
# res += num % 10
# print("Обратное число:", res)

# num1 = "2"
# num2 = 3
# res = int(num1) + num2
# # res = num1 + str(num2)
# print(res)

# print(int(3.981))
# print(type(round(3.581)))
# print(type(round(3.589, 2)))

# num1 = "2.5"
# num2 = 10
# res = float(num1) + num2  # 2.5 + 10
# print(res)

# name = "Виктор"
# age = 20
# print("Меня зовут", name, ". Мне", age, "лет.")
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print("Меня зовут ", name, ". Мне ", age, " лет.", end=" ", sep="")
# print("Hello Python")

# name = input("Введите имя: ")
# print("Hello,", name)


# num = int(input("Введите число: "))
# power = int(input("Введите степень: "))  # power = 2
# # num = int(num)
# # power = int(power)
# res = num ** power  # 5 ** 2
# print("Число", num, "в степени", power, "равно:", res)

# num1 = int(input("Введите число 1: "))
# num2 = int(input("Введите число 2: "))
# num3 = int(input("Введите число 3: "))
# num4 = int(input("Введите число 4: "))
# sum_1 = num1 + num2
# sum_2 = num3 + num4
# res = sum_1 / sum_2
# print(round(res, 2))

# b1 = True
# b2 = False
# # print(b1)
# # print(b2)
# # print(type(b1))
# # print(type(b2))
#
# # print(5 == 5)
# # print(5 == 3)
# print(int(b1))  # 1
# print(int(b2))  # 0
# print(b1 + 5)  # 1 + 5 = 6
# print(b2 + 5)  # 0 + 5 = 5

# print(bool("Python"))
# print(bool(""))
# print(bool(" "))
# print(bool(-5))
# print(bool(0))
# print(bool(0.2))
# print(bool(0.0))
# print(bool(True))
# print(bool(False))
# print(bool(None))


# test = None
# print(test)
# print(type(test))
# test = 5
# print(test)

# print(5 == 5)
# print(5 == 3)
# print(2 + 5 == 3 + 4)  # 7 == 7
# print(2 + 5 != 3 + 4)  # 7 != 7
# print(8 > 5)
# print(8 >= 8)
# print(5 < 10)
# print(5 <= 5)
# print("hello" > "Hello")  # 104 > 72

# print(2 < 4 < 9)  # True : True => True
# print(2 > 4 < 9)  # False : True => False
#
# print(2 * 5 > 7 >= 4 + 3)  # 10 > 7 >= 7  True : True => True
# print(3 * 3 <= 7 >= 2)  # 9 <= 7 >= 2  False : True => False


# n = int(input("Введите пятизначное число: "))  # 12345
# a = n % 10
# n //= 10
# b = n % 10
# n //= 10
# c = n % 10
# n //= 10
# d = n % 10
# n //= 10
# e = n % 10
# print("Произведение:", a * b * c * d * e)
# print("Среднее арифметическое:", (a + b + c + d + e) / 5)

# print(5 - 3 == 2 and 1 + 3 == 4)  # True and True  => True
# print(5 - 3 == 2 and 1 + 3 < 4)  # True and False  => False
# print(5 - 3 > 2 and 1 + 3 == 4)  # False and True  => False
# print(5 - 3 > 2 and 1 + 3 < 4)  # False and False  => False

# print(5 - 3 == 2 or 1 + 3 == 4)  # True and True  => True
# print(5 - 3 == 2 or 1 + 3 < 4)  # True and False  => True
# print(5 - 3 > 2 or 1 + 3 == 4)  # False and True  => True
# print(5 - 3 > 2 or 1 + 3 < 4)  # False and False  => False

# print(not 9 - 5)  # not True  => False
# print(not 7 - 7)  # not False => True

# a = 10
# b = 10
# if a > b:
#     print(a, ">", b)
# if b > a:
#     print(b, ">", a)
# if b == a:
#     print(b, "==", a)

# cnt = 5
# if cnt < 10:
#     cnt = cnt + 1
# else:
#     cnt = cnt - 1
# print(cnt)

# a = 40
# b = 50
# if a > b:
#     print(a, ">", b)
# elif b == a:
#     print(b, "==", a)
# else:
#     print(b, ">", a)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
#     print("Приятного просмотра")
# else:
#     print("Доступ запрещен")

# a = input("Введите первую строну: ")
# b = input("Введите вторую строну: ")
# c = input("Введите третью строну: ")
#
# if a == b == c:  # '10' == '10' == '10'
#     print("Треугольник равносторонний")
# elif a == b or a == c or b == c:
#     print("Треугольник равнобедренный")
# else:
#     print("Треугольник разносторонний")

# day = int(input("Введите день недели (цифрой): "))
# if 1 <= day <= 5:  # (day >= 1) and (day <= 5)
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#         print("среда")
#     if day == 4:
#         print("четверг")
#     if day == 5:
#         print("пятница")
# elif day == 6 or day == 7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("суббота")
#     if day == 7:
#         print("воскресенье")
# else:
#     print("Такого дня недели не существует")

# month = int(input('Введите номер месяца:'))
# if (month == 12) or 1 <= month <= 2:
#     print('Зима')
# if 3 <= month <= 5:
#     print('Весна')
# if 6 <= month <= 8:
#     print('Лето')
# if 9 <= month <= 11:
#     print('Осень')


# day = int(input('Ввведите номер месяца (цифрой): '))
# if 1 <= day <= 12:  # (day >= 1) and (day <= 5):
#     print('Время года - ', end='')
#     if day == 1 or day == 2 or day == 12:
#         print('Зима')
#     if 3 <= day <= 5:  # day == 4 or day == 5 or day == 3
#         print('Весна')
#     if day == 6 or day == 7 or day == 8:
#         print('Лето')
#     if day == 9 or day == 10 or day == 11:
#         print('Осень')
# else:
#     print('Такого времени года не существует')

# day = int(input('Ввведите номер месяца (цифрой): '))
#
# if day == 1 or day == 2 or day == 12:
#     print('Зима')
# elif 3 <= day <= 5:  # day == 4 or day == 5 or day == 3
#     print('Весна')
# elif day == 6 or day == 7 or day == 8:
#     print('Лето')
# elif day == 9 or day == 10 or day == 11:
#     print('Осень')
# else:
#     print('Такого времени года не существует')

# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
#     print("На ветке", end=" ")
#     if n == 1:
#         print(n, "ворона")
#     if 2 <= n <= 4:
#         print(n, "вороны")
#     if 5 <= n <= 9 or n == 0:
#         print(n, "ворон")
# else:
#     print("Ошибка ввода данных")

# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
#     print("На ветке", end=" ")
#     if n == 1:
#         print(n, "ворона")
#     elif 2 <= n <= 4:
#         print(n, "вороны")
#     else:
#         print(n, "ворон")
# else:
#     print("Ошибка ввода данных")


# match выражение:
#     case шаблон_1:
#         действие_1
#     case шаблон_2:
#         действие_2
#     case _:
#        действие по умолчанию

# password = "qwerty"
#
# match password:
#     case 'admin':
#         print("Администратор")
#     case 'user':
#         print("Пользователь")
#     case _:
#         print("Пароль не верен")

# day = 'вторник'
# time = 13
#
# match day:
#     case 'понедельник' | 'вторник' | 'среда' | 'четверг' | 'пятница' if 9 <= time <= 12 or 14 <= time <= 17:
#         print("Рабочий день")
#     case 'суббота' | 'воскресенье':
#         print("Выходной день")
#     case _:
#         print("Такого дня недели не существует или не рабочее время")

# a, b = 30, 20
#
# print(a if a < b else b)


# a, b = 20, 20
# print("a == b" if a == b else "a > b" if a > b else "b > a")

# a = int(input("Введите число от 1 до 99: "))  # 45
# kop = a  # 45
# if 11 <= kop <= 14:
#     print(a, "копеек")
# elif 1 <= a <= 99:
#     kop = kop % 10
#     if kop == 1:
#         print(a, "копейка")
#     elif 2 <= kop <= 4:
#         print(a, "копейки")
#     else:
#         print(a, "копеек")
# else:
#     print("Недопустимое значение")

# try:  # попытаться
#     n = int(input("Введите целое число: "))
#     print(n * 2)
# except ValueError:
#     print("Что-то пошло не так")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("Нельзя вводить строки")
# except ZeroDivisionError:
#     print("Нельзя делить на ноль")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Нельзя вводить строки или Нельзя делить на ноль")
# else:  # когда в блоке try не возникло исключения
#     print("Все нормально. Вы ввели числа", n, "и", m)
# finally:  # выполнится в любом случае
#     print("Конец программы")

# n = input("Введите первое число: ")  # '10'
# m = input("Введите второе число: ")  # qqq
#
# try:
#     n = int(n)  # 10
#     m = int(m)  #
# except ValueError:
#     n = str(n)
# finally:
#     print(n + m)

# Циклы

# while условие:
#     блок_инструкций

# i = 0  # счетчик
# while i < 5:  # условие
#     print("i =", i)
#     i += 1  # изменение счетчика


# итерация - один шаг цикла

# i = 0
# while i < 100:
#     print("i =", i)
#     i += 10


# i = 10
# while i > 0:
#     print("i =", i)
#     i -= 1

# i = 2
# while i <= 20:
#     if i % 2:  # i % 2 == 1, i % 2 != 0 - нечетные числа, i % 2 == 0 - четные числа
#         print(i, end=" ")
#     i += 1

# i = 2
# while i <= 20:
#     print(i, end=" ")
#     i += 2

# n = int(input("Количество символов: "))
# print("*" * n)
# i = 0
# while i < n:
#     print("*", end="")
#     i += 1

# +-+-+-+

# n = int(input("Количество символов: "))
# i = 0
# while i < n:
#     if i % 2 == 0:
#         print("+", end="")
#     else:
#         print("-", end="")
#     i += 1


# n = int(input("Количество символов: "))
# print("+" * n)


# n = int(input("Количество символов: "))
# while n > 0:
#     print("*", end="")
#     n -= 1

# a = int(input("Введите начало диапазона: "))
# b = int(input("Введите конец диапазона: "))
# res = 0
# while a <= b:
#     if a % 2:
#         print(a, end=" ")
#         res += a  # res = res + a
#     a += 1
# print("\nСумма:", res)

# n = input("Введите целое число: ")  # 'пять'
#
# while type(n) is not int:  # type(n) != int
#     try:
#         n = int(n)  # 8
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите целое число: ")  # '8'
#
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен")

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# while True:
#     n = int(input("Введите положительное число: "))
#     if n < 0:
#         break

# res = 1
# while True:
#     n = int(input("Введите число: "))
#     if n == 0:
#         break
#     res *= n  # res = res * n
# print("Результат:", res)

# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i =", i)

# i = 1
# while i < 5:  # 2
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:  # 1
#         print("\tВнутренний цикл: j =", j)
#         j += 1
#     i += 1


# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, end="\t\t")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 3:
#     j = 0
#     while j < 6:
#         print("^", end="")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if j % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1

# for element in collection:
#    print(element)

# for i in "Hello!", "World":
#     print(i)

# range(start=0, stop, step=1)

# a = 10
# for i in range(0, 10, 1):  # i = 0, i < 10, i += 1  # i = 10, i > 0, i -= 1
#     print(i, end=" ")
#
# print()
#
# i = 1
# while i < 10:
#     print(i, end=" ")
#     i *= 2


# a = int(input("Введите целое число: "))
#
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")

# for i in range(10, 100):
#     if i % 11 == 0:
#         print(i, end=" ")
#
# print()
#
# for i in range(11, 100, 11):
#     print(i, end=" ")
#
# print()
#
# for i in range(10, 100):
#     if i % 10 == i // 10:
#         print(i, end=" ")

# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print("Цикл закончен")

# for i in range(3):  # 3
#     print("+++")
#     for j in range(2):  # 0
#         print("-----")

# w = int(input("Введите ширину прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
#
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# letter = [i * 2 for i in "Hello"]
# print(letter)
#
# for i in "Hello":
#     print(i * 2)

# num = [i for i in range(30) if i % 2 == 0]
# print(num)
#
# for i in range(30):
#     if i % 2 == 0:
#         print(i, end=", ")


# Список (list)
# nums = [8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
# print(nums)
# print(type(nums))
# print(nums[0])
# print(nums[1])
# print(nums[10])
# print(nums[-1])
# # print(nums[len(nums)-1])
# print("Кол-во:", len(nums))
# nums[1] = 256
# nums[3] += 100
# print(nums)

# s = []
# print(s)
# print(type(s))
#
# t = list("Python")
# print(t)
# print(type(t))
#
# print(range(0, 8, 2))
# print(list(range(1, 18, 2)))

# a = [1, 3, 5, 7, 9]
# b = [11, 13, 15, 17]
# print(a + b)
# print(a * 3)

# a = [1, 3, 5, 7, 9]
#
# for i in a:
#     print(i)

# a = [0 for _ in range(5)]
# print(a)  # [0, 0, 0, 0, 0]

# a = [i for i in range(5)]
# print(a)  # [0, 1, 2, 3, 4]

# n = 15
# a = [i ** 2 for i in range(2, n)]
# print(a)  # [0, 1, 2, 3, 4]

# a = [0] * int(input("Введите количество элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("-> "))
# print(a)

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)

# lst = [9, 6, 3, 5]
#
# for i in range(len(lst)):  # 0 1 2 3
#     print(lst[i], end=" ")
#
# print()
#
# for v in lst:  # 9 6 3 5
#     print(v, end=" ")

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# res = 0
# # for i in range(len(a)):  # 0 1 2 3 4
# #     if a[i] < 0:
# #         res += a[i]
#
# for i in a:  # 9, -2, 7, -3, 4
#     if i < 0:
#         res += i
#
# print(res)


# n = list(range(21, 41))
# print(n)
# count = sum_ = 0
# # for i in range(len(n)):
# #     if n[i] % 2 == 0:
# #         count += 1
# #     else:
# #         sum_ += n[i]
#
# for i in n:
#     if i % 2 == 0:
#         count += 1
#     else:
#         sum_ += i
#
# print("Количество четных элементов списка:", count)
# print("Сумма нечетных элементов списка:", sum_)

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# for i in range(len(a)):
#     if i % 2 == 0:
#         print(a[i], end=" ")
# print()
#
# for i in range(0, len(a), 2):
#     print(a[i], end=" ")

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end=" ")

# a = [9, 7, 8, 4, 2]
# print(a)
# a[0], a[1] = a[1], a[0]
# print(a)

# Срез

# список[start:stop:step]
# a = [9, 7, 8, 4, 2, 1, 3]
# print(a)
# print(a[1:4])
# print(a[5:])
# print(a[1:4:2])
# print(a[::-2])
# print(a[-1:0:-1])
# print(a[10:20])

# lst = list(range(1, 8))
# print(lst)
# print(lst[::-1])
# print(lst[::2])
# print(lst[1::2])
# print(lst[:1])
# print(lst[-1:])
# print(lst[3:4])
# print(lst[4:])
# print(lst[4:1:-1])
# print(lst[2:5])

# a = [1, 2, 3, 4, 5, 6, 7]
# print(a)
# a[1:3] = [0, 0, 0, 0]
# print(a)
# a[1:2] = [20]
# print(a)
# a[2] = [120, 45]
# print(a)

# a[100:111] = [100]
# print(a)
# print(a[9])
# print(len(a))

# Методы списков
# print(dir(list))
# ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# s = [9, 7, 8, 4, 2, 1, 3]
# print(s)
# s.append(99)  # добавляет элемент в конец списка
# print(s)
# s.extend([11, 12, 13])  # добавляет список элементов в конец списка
# print(s)
# s.insert(2, 100)  # добавляет элемент (второй параметр) по заданном индексу (первый параметр)
# print(s)

# s.insert(20, 5)
# print(s)

# s = []
# n = int(input("Количество элементов в списке: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     # s.append(x)
#     s.insert(0, x)  # [7, 8, 9]
# print(s)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7, 2]
# c = []  # [2, 1, 4, 3]
#
# for i in a:  # 2
#     for j in b:  # 2
#         if i in c:
#             continue
#         if i == j:  # 2 == 2
#             c.append(i)
#             break
# print(c)

# a = [5, 9, 2, 1, 4, 3, 2, 4]  #
# b = [4, 2, 1, 3, 7, 2]  #
# c = []
#
# for i in a:
#     if i in b and i not in c:
#         c.append(i)
# print(c)

# a = [1, 2, 3]
# b = [11, 22, 33, 4, 2]
# c = []
#
# if len(b) > len(a):
#     for i in range(len(a)):  # 0, 1, 2, 3, 4
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append(b[i])
# else:
#     for i in range(len(b)):  # 0, 1, 2, 3, 4
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
#
# print(c)

# a = [1, 2, 3, 4, 2]
# b = [11, 22, 33]
# c = []
#
# if len(a) > len(b):
#     a, b = b, a
#
# for i in range(len(a)):  # 0, 1, 2, 3, 4
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):
#     c.append(b[i])
#
# print(c)

# s = [9, 7, 8, 4, 2, 8, 1, 3]
# print(s)
# item = 7
# if item in s:
#     s.remove(item)  # удаляет первое вхождение элемента по значению
# print(s)

# last = s.pop()  # удаляет последний элемент из списка
# print(last)
# print(s)
#
#
# try:
#     second = s.pop(10)  # удаляет элемент по заданному индексу
# except IndexError:
#     second = "Такого индекса нет"
# print(second)
# print(s)
#
# s.clear()  # удаляет элементы из списка
# print(s)

# s = [9, 7, 8, 4, 2, 8, 1, 3]
# print(s)
#
# s[5:] = []
# print(s)
#
# del s[:]
# print(s)

# s = [9, 7, 8, 4, 2, 8, 1, 3, 8]
# print(s)
#
# # num = s.count(9)  # количество вхождений заданного элемента
# # print(num)
#
# ind = s.index(8, 3, 7)  # ищет первое вхождение заданного элемента, возвращает индекс на котором
# # нашел элемент, можно задать диапазон поиска
# print(ind)

# m = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# print(m)
# for i in m:
#     if m.count(i) == 1:
#         print(i, end=" ")
# print()
# mas = [i for i in m if m.count(i) == 1]
# print(mas)

# a = [1, 2, 3]
# b = a.copy()
# print("a =", a, id(a))
# print("b =", b, id(b))
# b.append(20)
# print("a =", a)
# print("b =", b)
# a.append(100)
# print("a =", a, id(a))
# print("b =", b, id(b))


# m = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# # print(m)
# # m.reverse()
# # # print(m)
# m.sort(reverse=True)
# print(m)
#
# # s = ["Виталий", "Сергей", "Александр", "Анна"]
# # s.sort(key=len, reverse=True)
# # print(s)
#
# s = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
#
# print("lst:", sorted(s, reverse=True))
# print(s)
# print()


# import random

# print(random.random())
# print(random.randint(5, 10))
# print(random.randrange(5, 10, 2))
# print(round(random.uniform(10.5, 25.5), 2))

# city_list = ["Москва", "Новосибирск", "Воронеж", "Сочи", "Екатеринбург"]
# s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# print(random.choice(city_list))
# print(random.choice(s))
# print(random.choices(city_list, k=3))
# print(random.choices(s, k=3))
# random.shuffle(s)
# print(s)


# import random
#
# mas = [random.randint(50, 100) for i in range(5)]
# print(mas)
# print(len(mas))
# print(max(mas))
# print(min(mas))
# print(sum(mas))

# import random
# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)
# max_ = max(mas)
# print(max_)
# mas.remove(max_)
# mas.insert(0, max_)
# print(mas)


# import random
# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)
#
# min_ = min(mas)
# print("Min:", min_)
#
# ind = mas.index(min_)
# print("Index min:", ind)
#
# del mas[:ind]
# print(mas)


# m = [
#     [1, 2, 3, 4],  # 0
#     [5, 6, 7, 8],  # 1
#     [9, 10, 11, 12]  # 2
# ]
# print(m)
#
# # print(len(m))
# # print(m[1][2])
# # print(m[2][1])
#
# print("Вариант 1")
# for row in range(len(m)):
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t")
#     print()
# print("Вариант 2")
# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()

# m = ["Hello", "World", [44, [1, 2, 3], 55, ["Python", "new"]]]
# print(m)
# print(m[1][2])
# print(m[2][1][1])
# print(m[2][3][0][3])

# import math
#
# print(math.sqrt(4))
# print(math.ceil(3.2))
# print(math.floor(3.8))


# import math as m
#
# print(m.sqrt(4))
# print(m.ceil(3.2))
# print(m.floor(3.8))

# from math import *
#
# print(sqrt(4))
# print(ceil(3.2))
# print(floor(3.8))

# from math import sqrt, ceil, floor
#
# print(sqrt(4))
# print(ceil(3.2))
# print(floor(3.8))
# import math
# print(dir(math))

# from math import pi
#
# # print(pi)
# radius = int(input("Введите радиус окружности: "))
# print("Длина окружности:", round(2 * radius * pi, 2))

# import time
# import locale

# print(time.time())
# print(time.ctime(739210060))
# res = time.localtime()
# print(res)
# print(res.tm_year, "-", res.tm_mon, "-", res.tm_mday, sep="")
# print(time.strftime("Today is %B %d, %Y"))
# # print(time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime(539210060)))
# locale.setlocale(locale.LC_ALL, "ru")
# print(time.strftime("Сегодня: %B %d, %Y"))

# start = time.time()
# print("Запуск программы")
# time.sleep(5)
# res = time.time() - start
# print("Программа выполнилась за", res, "сек.")

# import math
# from math import sqrt, pi
#
s = None
shape = int(input("Выбор фигуры:\n1-треугольник\n2-прямоугольник\n3-круг\n: "))
if shape == 1:
    a = int(input("Введите строну a = "))
    b = int(input("Введите строну b = "))
    c = int(input("Введите строну c = "))
    p = (a + b + c) / 2
    s = sqrt(p * (p - a) * (p - b) * (p - c))
elif shape == 2:
    a = int(input("Введите строну a = "))
    b = int(input("Введите строну b = "))
    s = a * b
elif shape == 3:
    radius = int(input("Введите радиус = "))
    s = pi * radius ** 2
else:
    print("Такой фигуры нет")

print(round(s, 2))


# Функции

# def hello(first_name, age):   # аргументы
#     print("Меня зовут:", first_name, "Мой возраст:", age)
#
#
# hello("Irina", 28)  # параметры
# hello("Ivan", 25)


# def get_sum(a, b):
#     print(a + b)
#
#
# x = 2
# y = 5
# get_sum(x, y)
# get_sum("abc", "def")


# def symbol(count, a, b):
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end="")
#         else:
#             print(b, end="")
#     print()
#
#
# symbol(9, "+", "-")
# symbol(7, "X", "0")

# def get_sum(a, b):
#     print("Сумма:", end=" ")
#     c = a + b
#     return c
#
#
# x = 2
# y = 5
# res = get_sum(x, y)
# print(res)

# def maximum(one, two):
#     if one > two:
#         return one
#     else:
#         return two
#
#
# print(maximum(9, 5))
# print(maximum(5, 15))

# def zadacha(a, b):
#     if a > b:
#         return a - b
#     else:
#         return a + b
#
#
# x = int(input("a = "))
# y = int(input("y = "))
# print(zadacha(x, y))


# def cube(a):
#     return a * a * a
#
#
# for i in range(1, 11):
#     print(i, "в кубе =", cube(i))

# def change(lst):
#     end = lst.pop()
#     start = lst.pop(0)
#     lst.append(start)
#     lst.insert(0, end)
#     return lst

# def change(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(["с", "л", "о", "н"]))

# def one_big(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# if one_big(a, b):
#     print("Первое число больше второго")
# else:
#     print("Второе число больше первого")

# print(one_big(10, 5))
# print(one_big(5, 10))

# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":  # "A" <= "S" <= "Z"
#             has_upper = True
#         if "a" <= ch <= "z":
#             has_lower = True
#         if "0" <= ch <= "9":  # "0" <= "8" <= "9"
#             has_num = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Это надежный пароль")
# else:
#     print("Это ненадежный пароль")

# res = 10
#
#
# def get_sum(a, b, c=0, d=1):
#     inner = 20
#     return a + b + c + d + res + inner
#
#
# print(get_sum(1, 5, 2, 7))

# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# print(get_sum(1, 5, d=2, c=5))
# print(get_sum("С", "л", d="н", c="о"))


# def set_param(count=20, symbol="-"):
#     print(symbol * count)
#
#
# set_param(10, "+")
# set_param(5, "*")
# set_param(15, "#")
# set_param(7)
# set_param()


# def display_info(name, age):
#     print("Name:", name, "\nAge:", age)
#
#
# display_info("Irina", 23)
#
#
# def display_info(name, age):
#     print("Hello,", name)
#
#
# display_info("Irina", 23)
# display_info(23, "Irina")
# display_info(age=23, name="Irina")
# display_info("Igor", age=23, name="Irina")


# lt1 = "Hello"
# lt2 = "Hello"
# print(lt1, id(lt1))
# print(lt2, id(lt2))
# print(lt1 == lt2)
# print(lt1 is lt2)
#
# lst1 = [1, 2, 3]
# lst2 = [1, 2, 3]
# print(lst1, id(lst1))
# print(lst2, id(lst2))
# print(lst1 == lst2)
# print(lst1 is lst2)

# lst1 = [1, 2, 3]
# print(lst1, id(lst1))
# lst1.append(4)
# print(lst1, id(lst1))
# lst1.pop(1)
# print(lst1, id(lst1))

# lt1 = "Hello"
# print(lt1, id(lt1))
# lt1 = lt1[5:10]
# print(lt1, id(lt1))
# lt1 = lt1 + "!"
# print(lt1, id(lt1))

# a = 5
# print(a, id(a))
# a = 7
# print(a, id(a))


# Кортеж (tuple)

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())
# lst[1] = 100
# print(lst)

# a = ()
# print(a, type(a))
# b = tuple()
# print(b, type(b))


# a = (1, 2, 3)
# print(a, type(a))
#
# b = tuple("Hello")
# print(b, type(b))


# b = tuple("Hello")
# print(b)
#
# print(b[1])
# print(b[1:3])

# s1 = tuple(input("-> ") for i in range(5))
# print(s1)

# s1 = tuple(i for i in range(5))
# print(s1)

# from random import randint
#
# s1 = tuple(randint(50, 100) for i in range(5))
# print(s1)

# t1 = tuple("hello")
# t2 = tuple("world")
# print(t1)
# print(t2)
# t3 = t1 + t2
# print(t3 * 2)
# print(t3)
# print(t3.count("a"))
# print(t3.index("l", 4, -2))
# print(dir(list))
# print(dir(tuple))

# v = "a"
# if v in t3:
#     print(t3.index(v))
# else:
#     print("Такого символа нет")


# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) == 1:
#             return tpl[tpl.index(el):]  # tpl[2:]
#         else:
#             first = tpl.index(el)
#             second = tpl.index(el, first + 1) + 1  # tpl[5]
#             return tpl[first:second]  # [1:5]
#     else:
#         return tuple()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# t = (10, "Python", True, [1, 2, 3], ["hello", "world"])
# print(t, id(t))
# t[4][0] = "new"
# print(t, id(t))
# print(len(t))
# t[4].append("hi")
# print(t, id(t))

# Распаковка кортежа

# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t  # Распаковка кортежа
# # x, y, z = 1, 2, 3
# print(x, y, z)


# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# # user = get_user()
# # print(user)
# # first_name, year, married = user
#
# first_name, year, married = get_user()
# print(first_name, year, married)


# lst = [1, 2, 3, 4, 5, 6]
# print(lst, type(lst))
# tpl = tuple(lst)
# print(tpl, type(tpl))
# lst2 = list(tpl)
# print(lst2, type(lst2))

# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
# )
# print(countries, end="\n\n")
#
# for county in countries:
#     county_name, county_population, cities = county
#     print("\nСтрана: ", county_name, ", население = ", county_population, sep="")
#     for city in cities:
#         city_name, city_population = city
#         print("\tГород: ", city_name, ", население = ", city_population, sep="")


# tpl = tuple(input("Введите строку: "))
# print(tpl)
#
# lst = []
# for i in range(len(tpl)):
#     if tpl[i] not in lst:
#         lst.append(tpl[i])
#
# for i in range(len(lst)):
#     print("Количество", lst[i], "=", tpl.count(lst[i]))


# Множество (set)

# s = {"red", "yellow", "green", "yellow", "green"}
# print(s, type(s))
# print(len(s))

# a = set("hello")
# print(a, type(a))

# s = {x * x for x in range(10)}
# print(s)

# lst = [1, 2, 2, 2, 2, 3, 3, 4, 4, 4, 5, 6]
# lst = ["red", "yellow", "green", "yellow", "green"]
# print(lst)
# num = set(lst)
# print(num)
# lst2 = list(num)
# print(lst2)

# t = {'yellow', 'red', 'green'}
# print('red' in t)
# print('blue' in t)
# for i in t:
#     print(i)


# lst = ['ab_1', "ac_1", 'bc_1', 'bc_2']
# print({i for i in lst if 'a' in i})
# print(['A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in lst])
# tpl = tuple('A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in lst if i[1] == 'c')
# print(tpl)

# print(dir(set))

# a = {"red", "yellow", "green"}
# print(a)
# a.add("blue")
# print(a)
# # a.remove("yellow")
# # a.remove("black")  # KeyError
# color = "black"
# # if color in a:
# #     a.remove(color)
# # a.discard(color)
# # a.pop()
# a.clear()
# print(a)


# print({i / 2 for i in range(1000, 1010)})

# from random import randint
#
#
# def ran(a, b):
#     return tuple(randint(a, b) for i in range(10))
#
#
# tpl1 = ran(0, 5)
# print(tpl1)
# tpl2 = ran(-5, 0)
# print(tpl2)
# tpl3 = tpl1 + tpl2
# print(tpl3)
# print("0 =", tpl3.count(0))

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# # c = a.union(b)
# # c = a | b  # {0, 1, 2, 3, 4}
# # print(c)#
# # c = a & b  # {1, 2, 3}
# # print(c)
# # c = a - b  # {0}
# # print(c)
# c = a ^ b  # {0}
# print(c)
# # a |= b
# # print(a)
# # a &= b
# # print(a)
# # a -= b
# # print(a)
# a ^= b
# print(a)

# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
# c = a >= b
# print(c)

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# c = {6, 2}
# e = {8, 2}
# d = b ^ c ^ a ^ e  # {0, 4, 6, 8}
# d = a.symmetric_difference(b).symmetric_difference(c).symmetric_difference(e)  #
# print(d)

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {1, 2}
# s7 = {1, 2}

# a = {1, 2}
# b = {3}
# c = {4, 5}
# d = {3, 2, 6}
# e = {6}
# f = {7, 8}
# g = {9, 8}
# su = a.symmetric_difference(b).symmetric_difference(c).symmetric_difference(d).symmetric_difference(
#     e).symmetric_difference(f).symmetric_difference(g)
# print(su)
# print(len(su))
# print(min(su))
# print(max(su))

# a = {1, 2}
# b = {3}
# c = {4, 5}
# d = {3, 2, 6}
# e = {6}
# f = {7, 8}
# g = {9, 8}
# h = a | b | c | d | e | f | g
# print(h)
# print('Unic elems count', (len(h)))
# print('Min elem: ', min(h))
# print('Max elem: ', max(h))

# s1 = "Hello"
# s2 = "How are you"
# s3 = set(s1) & set(s2)
# print(s3)
# for i in s3:
#     print(i, end=" ")

# s = frozenset([1, 2, 3, 4, 5, 6])
# print(s)
# s1 = frozenset("hello")
# print(s1)


# Словарь (dict)

# lst = ["one", "two"]
# d = {"first": "one", "second": "two"}
#
# print(lst[1])
# print(d["second"])

# d = {0: "text", "one": 45, (1, 2): "Кортеж", True: [5, 9, 8, 7, 7], False: "один", 1: "Список"}
# print(d)


# d = {1: "one", "second": "two"}
# print(d)
# print(type(d))
#
# d1 = dict(first="one", second="two")
# print(d1)
# print(type(d1))

# lst = [
#     ["one", 1],
#     ["two", 2],
#     ["three", 3]
# ]
#
# print(lst)
# d = dict(lst)
# print(d)

# d = {i: i ** 2 for i in range(1, 7)}  # 1,2,3,4,5,6
# print(d)
#
# for i in d:
#     print("key =", i, "value =", d[i])

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# res = 1
# for key in d:
#     res *= d[key]
#
# print(res)

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# print(d)
# del d["x2"]
# print(d)

# d = dict()
# d[1] = input("-> ")
# d[2] = input("-> ")
# d[3] = input("-> ")
# d[4] = input("-> ")
# print(d)

# d = {i: input("-> ") for i in range(1, 5)}
# print(d)
# dislike = int(input("Какой элемент исключить: "))
# del d[dislike]
# print(d)

# goods = {
#     "1": ['Core-i3-4330', 9, 4500],
#     "2": ['Core i5-4670K', 3, 8500],
#     "3": ['AMD FX-6300', 6, 3700],
#     "4": ['Pentium G3220', 8, 2100],
#     "5": ['Core i5-4350', 5, 6500],
# }
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], "руб", sep="")
#
# while True:
#     n = input("№: ")
#     if n == "0":
#         break
#     else:
#         if n in goods:
#             while True:
#                 try:
#                     count = int(input("Количество: "))
#                     goods[n][1] += count
#                     break
#                 except ValueError:
#                     print("Значение некорректно. Введите число")
#         else:
#             print("Такого ключа не существует")
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], "руб", sep="")

# print(dir(dict))


# d = {1: "one", 2: "two", 3: "three"}
# print(d.keys())
# print(d.values())
# print(d.items())
#
# for i, j in d.items():
#     print(i, ":", j)

# d = {1: "one", 2: "two", 3: "three"}
# d2 = d.copy()
# print("D =", d)
# print("D2 =", d2)
#
# d2[2] = "four"
# print("D =", d)
# print("D2 =", d2)


# d = {1: "one", 2: "two", 3: "three"}
# print(d)
# # d.clear()
# item = d.pop(6, "Такого ключа не существует")
# print(d)
# print(item)
#
# d = {1: {11: "one", 2: "two", 3: "three"}}
