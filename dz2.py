class Student:
    def __init__(self, name, laptop):
        self.name = name
        self.laptop = laptop

    def display_info(self):
        print(f"Студент => {self.name}")
        self.laptop.display_info()

class Laptop:
    def __init__(self, brand, processor, memory):
        self.brand = brand
        self.processor = processor
        self.memory = memory

    def display_info(self):
        print(f"Ноутбук: {self.brand}, Процессор: {self.processor}, Память: {self.memory} ГБ")

# Пример использования
roman_laptop = Laptop("HP", "i7", 16)
roman = Student("Роман", roman_laptop)

vladimir_laptop = Laptop("HP", "i7", 16)
vladimir = Student("Владимир", vladimir_laptop)

# Вывод информации
roman.display_info()
vladimir.display_info()
