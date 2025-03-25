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

# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, I =", i  )

# i = 1
# while i < 5:
#     print("Внешний цикл i = ", i)
#     j = 1
#     while j < 4:
#         print("\t Внутртиний цикл: j = ", j)
#         j += 1
#     i += 1

# i = 1
# while i < 9:
#     j = 1
#     while j < 10:
#         print(i ,"*", j, "=", i * j, end="\t\t" )
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 4:
#     j = 0
#     while j < 16:
#         if j % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j+=1
#     print()
#     i += 1

# for elment in  collection
#     print(element)

# for i in "Hello", "world":
#     print(i)

# range ( start , stop, step)

# print(range(0, 8 , 2))

# a = 10
# for i in range (0, 10, 1):# i 0. i <10 , i += 1
#     print(i, end=" ")
#
# print()
#
# i = 1
# while i < 10:
#     print(i, end=" ")
#     i *= 2

# a = int(input("Введите целое цисло: "))
#
# for i in range(1, a+1):
#     if a % i == 0:
#         print(i, end=" ")

# for i in range(10, 100):
#     if i % 11 == 0:
#         print(i, end = " ")
# print()
#
# for i in range(10, 100, 11 ):
#         print(i, end=" ")
# print()
# for i in range (10, 100):
#     if i % 10 == i // 10:
#         print(i, end=" ")


# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print("Цикл закончен")

# for i in range(3):
#     print("+++")
#     for j in range(2):
#         print("----")

# w = int(input("Ширина :"))
#
# h = int(input("Высота: "))
#
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w -1:
#
#             print("*", end="")
#         else:
#             print("", end=" ")
#     print()


# letter = [i*2 for i in "hello"]
# print(letter)
#
# for i in "hello":
#     print(i*2)

# num = [i for i in range(30) if i % 2 == 0]
# print(num)


# num = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28] # list- список
# print(num)
# print(type(num))
# print(num[0])# обращение к индексу
# print(num[-1])
# print("Кол-во" , len(num))# длина списка = последний индекс / последний индекс = длина списка -1
#
# num[1]=256
# num[3] += 100
# print(num)

# s = []
# print(s)
# print(type(s))
#
# t= list("hello")
# print(t)
# print(type(t))
#
# print(range(0, 8, 2))
#
# print(list(range(0, 18, 2)))

# a = [0, 2, 4, 6, 8, 10, 12, 14, 16]
# b = [1, 4, 5, 6, 10,13, 16, 15, 50 ]
# print(a+b)
# print(a*-3)

# a = [1, 3, 5, 7, 9]
#
# for i in a:
#     print(i)

# a= [0 for i in range(5)]
# print(a)   # получаем список из 5 нулей

# n = 5
# a= [i**2 for i in range(n)]
# print(a)

# a = [0] * int(input("Введите кол-во элементов:"))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("--->"))
# print(a)

# a = [int(input("-->")) for i in range(int(input("n=")))]
# print(a)

# lst = [9, 6, 3, 5]
# for i in range(len(lst)):
#     print(lst[i], end= " ")
#
# print()
#
# for k in lst:
#     print(k, end=" ")

# n = list(range(21, 41))
# print(n)
# count = sum_ = 0
# for i in range(len(n)):
#     if n[i] % 2 == 0:
#         count += 1
#     else:
#         sum_ += n[i]
# print("Колличество четных:", count)
# print("Сумма нечетных: ", sum_)

# a = [int(input("->")) for i in range(int(input("n = ")))]
# print(a)
# for i in range(len(a)):
#     if a[i] % 2 == 0:
#         print(a[i], end=" ")
# print()
#
# for i in range(0, len(a), 2):
#     print(a[i], end=" ")
#

# a = [int(input("->")) for i in range(int(input("n = ")))]
# print(a)
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end=" ")
#
# for i in range(len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end=" ")
# for i in a:
#     if i > i - 1:
#         print(i, end=" ")

# a = [9, 7, 8, 4, 2]
# print(a)
# a[0], a[1] = a[1], a[0]
# print(a)

# список[start:stop:step]

# a = [9, 7, 8, 4, 2, 1,3]
# print(a)
# print(a[1:4])
# print(a[5:])
# print(a[1:4:2])
# print(a[5:2:-1])

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

# lst = list(range(1, 8))
# print(lst)
# lst[1:2] = [0, 0, 0, 0]
# print(lst)
# lst[1:2]=[20]
# print(lst)
# lst[2]=[120, 45]
# print(lst)
# lst[10:11]=[100]
# print(lst)
# print(lst[-1])
# print(len(lst))

# методы списков

# print(dir(list))
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

# s = [9, 7, 8, 4, 2, 1, 3]
# s.append(99)  # Добовляет элемент в конец списка
# print(s)
# s.extend([11, 12, 13])#Добовляем список элементов в конец списка
# print(s)
# s.insert(0,100) # добавляет элемент(второй параметр) по заданному индексу (первый параметр)
#
# s.insert(-1,5)
# print(s)

# s = []
# n= int(input("Кол-во элементов в списке:"))
# for num in range(n):
#     x=int(input("Введите число:"))
#     # s.append(x)
#     s.insert(0, x)
# print(s)

# a = [5, 9, 2, 1, 4, 3]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i == j:
#             c.append(i)
#             break
# print(c)

# a = [5, 9, 2, 1, 4, 3]
# b = [4, 2, 1, 3, 7,2]
# c = []
# for i in a:
#     if i in b and i not in a:
#         c.append(i)
# print(c)

# a = [1, 2, 3,]
# b = [11, 22, 33,4, 2]
# c = []
# if len(b)>len(a):
#     for i in range(len(a)):  # 0. 1 . 2
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b))
#         c.append(b[i])
# else:
#     for i in range(len(b))
#         c.append(a[i])
#         c.append(b[i])
#     for
# print(c)

# s = [9, 7, 8, 4, 2, 1,8, 3]
# print(s)
# item = 7
# if item in s:
#     s.remove(8) #удаляет первое входные элемента по значению
#
# print(s)
#
# # last = s.pop() # удаляет последний элемент из списка
# # print(last)
# # print(s)
# try:
#     second=s.pop(1)# удаляет элемент по заданому индексу
#     print(second)
# except IndexError:
#     second = "Такого индекса нет"
# print(second)
# print(s)
#
# s.clear()#удаляет элементы из списка
# print(s)

# s = [9, 7, 8, 4, 2, 1, 8, 3]
# print(s)
# s[5:] = []
# print(s)
# del s[:]
# print(s)
#
# s = [9, 7, 8, 4, 2, 1, 8, 3]
# print(s)
# num=s.count(8) # считает кол-во заданных элементов
# print(num)

# ind = s.index(8, 3, 7) # ищет первое вхождение заданного элемента возвращает индекс на котором
# # нашел элемент, можно задать диапазон поиска


# a = [1, 2, 3]
# b = a
# print("a=", a)
# print("b= ", b)
# b.append(20)
# print("a=", a)
# print("b= ", b)
# a.append(100)
# print("a=", a)
# print("b= ", b)


