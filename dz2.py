class car:
    marka = "X7 m501"
    year = "2021"
    car = "BMW"
    model = "530 л.с "
    colour = "Белый"
    price = "1079000 рублей"

    def print_info(self):
        print(" Данные автомобиля".center(40, "*"))
        print(f"Название модели:{self.marka}\n"
              f"Год выпуска:{self.year}\n"
              f"Производитель:{self.car}\n"
              f"Мощность ДВС:{self.model}\n"
              f"Цвет машины:{self.colour}\n"
              f"Цена:{self.price}")
        print("=" * 40)


r1 = car()
r1.print_info()