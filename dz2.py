class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


    def __str__(self):
        return f"{self.name}, {self.age} лет"


class Pupil(Person):


    def __init__(self, name, age, group, level):
        super().__init__(name, age)
        self.group = group
        self.level = level


    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}, учится в группе {self.group}, уровень {self.level}"


class Educator(Person):


    def __init__(self, name, age, department, level):
        super().__init__(name, age)
        self.department = department
        self.level = level


    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}, работает в {self.department}, уровень {self.level}"


class Alumnus(Person):


    def __init__(self, name, age, field, level):
        super().__init__(name, age)
        self.field = field
        self.level = level


    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}, работает в области {self.field}, уровень {self.level}"


members = [
    Pupil("Батодадаев Даши", 16, "Web_011", 5),
    Educator("Загдулин Линар", 32, "РПО PD_011", 5),
    Pupil("Шугани Сергей", 15, "РПО PD_011", 5),
    Alumnus("Даншин Андрей", 38, "Астрофизика", 110),
    Pupil("Маркин Даниил", 17, "Python_011", 5),
    Educator("Баширов Алексей", 45, "Программирование", 20)
]


for member in members:
    print(member)
