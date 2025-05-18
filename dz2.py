import json


class DataManager:
    @staticmethod
    def load_data():
        try:
            with open("data.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    @staticmethod
    def save_data(data):
        with open("data.json", "w") as file:
            json.dump(data, file)

    @staticmethod
    def add_data(data):
        country = input("Введите название страны : ")
        capital = input("Введите название столицы страны : ")
        data[country] = capital
        DataManager.save_data(data)
        print("Данные добавлены.")

    @staticmethod
    def delete_data(data):
        country = input("Введите название страны для удаления: ")
        if country in data:
            del data[country]
            DataManager.save_data(data)
            print("Данные удалены.")
        else:
            print("Страна не найдена.")

    @staticmethod
    def search_data(data):
        country = input("Введите название страны для поиска: ")
        if country in data:
            print(f"Столица {country}: {data[country]}")
        else:
            print("Страна не найдена.")

    @staticmethod
    def edit_data(data):
        country = input("Введите название страны для редактирования: ").lower()
        if country in data:
            new_capital = input("Введите новое название столицы: ").lower()
            data[country] = new_capital
            DataManager.save_data(data)
            print("Данные обновлены.")
        else:
            print("Страна не найдена.")

    @staticmethod
    def view_data(data):
        if data:
            for country, capital in data.items():
                print(f"{country}: {capital}")
        else:
            print("Нет данных.")


def main():
    data = DataManager.load_data()
    while True:
        print("\nВыбор действия:")
        print("1 - добавление данных")
        print("2 - удаление данных")
        print("3 - поиск данных")
        print("4 - редактирование данных")
        print("5 - просмотр данных")
        print("6 - завершение работы")
        choice = input("Ввод: ")

        if choice == "1":
            DataManager.add_data(data)
        elif choice == "2":
            DataManager.delete_data(data)
        elif choice == "3":
            DataManager.search_data(data)
        elif choice == "4":
            DataManager.edit_data(data)
        elif choice == "5":
            DataManager.view_data(data)
        elif choice == "6":
            print("Работа завершена.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()