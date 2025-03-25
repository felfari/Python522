# print(bin(18))
# print(oct(18))

# def charge(s, old, new):
#     s2 = ""
#     i = 0
#     while i < len(s):
#         if s[i] == old:
#             s2 += new
#         else:
#             s2 += s[i]
#         i += 1
#
#
#     return s2
#
# str1 = "Я изачаю Nuthon. Мне нравиться Nuthon"
# str2 = charge(str1, "N", 'P')
# print(str1)
# print(str2)


# print("c:\\file.txt")

# num = 74
# print(f"{{{{{num}}}}}")


# dir_name="Folder"
# file_name="file.txt"
# print(fr"home\{dir_name}\{file_name}")
# print(fr"home\\"+ dir_name+"\\"+file_name)

#
# s = """многострочный текст
# """
# print(s)
# st = (""многострочный текст"-
# "")


# def squre(n):
#     return n**2
#
#
# print(squre(5))
# # print(squre.__doc__)
# # print(sum.__doc__)
# print(min.__doc__)

from math import pi
from sqlite3.dbapi2 import paramstyle

# def cylindr(r, h):
#     """
#
#     :param r:
#     :param h:
#     :return 2*pi*r*(r+h)
#     """
#
#
# print(*cylindr(2, 4))


# print(ord("a"))
# print(ord("п"))

# st = "Test string for me"
#
# arr = [ord(x) for x in st]
# print("Ascii коды: ", arr)
# arr = [int(sum(arr) / len(arr))]+arr
# print('среднее ариф-кое:', arr)
# arr+=[x for x in input("->")]
# print(arr)

# print(chr(97))
# print(chr(35))
# print(chr(8364))

# a = 122
# b = 97
# if a>b:
#     for i in range(b, a + 1):
#         print(chr(i), end=" ")
# else:
#     for i in range(a,b+1):
#         print(chr(i), end=" ")
#
# print("apple"== "Aplle")
# print(ord('a'))
# print(ord("A"))


from random import randint

short = 8
long = 16
min_ascii = 33
max_ascii = 123

# def randon_password():
#     rand_len= randint(short,long)
#     result=" "
#     result = " "
#     for i in range(6):
#         result += chr(randint(min_ascii, max_ascii))
#     return result
#
#
# print("Пароль:", randon_password())

s = "Hello, WORLD! I am learning Python."
# print(s.capitalize())
# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())


# print(s.count('h', __start: 1, -4))
# print(s.lower().count('i'))

# print(s.find("Python"))
# print(s.find('h',1,4))
#
#
# print(s.index('Python'))
# print(s.index('h',1,4))


# st='один два '
# one = st[:st.find('  ')]
# two = st[st.find('')+1:]
#
# print(two)


# print(s.find("h"))

# st = "I am learning Python. hello, WORLD!"
# print(st[:st.find('h')] + st[st.rfind("h")+1:])


# print('abc123'.isalnum())
#
#
# print("ABCsvb".isalpha())


st = " Никонов Валерий Анатольевич "
st = st.split()
print(f"st{[0]} {st[1][1]}.{st[2][0]}.")
