from Model import Film
from Model import Model
from view import View

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def run(self):
        while True:
            choice = self.view.show_menu()
            match choice:
                case '1':
                    data = self.view.get_film_details()
                    if data:
                        self.model.add_film(data)
                        self.view.show_message(" Фильм успешно добавлен!")

                case '2':
                    self.view.show_all(self.model.get_all_films())
                case '3':
                    title = self.view.get_title_input()
                    film = self.model.get_film(title)
                    self.view.show_film(film)
                case '4':
                    title = self.view.get_title_input()
                    if self.model.delete_film(title):
                        self.view.show_message(" Фильм удален.")
                    else:
                        self.view.show_message("Фильм не найден.")
                case 'q' | 'Q':
                    self.view.show_message("Выход из программы")
                    break
                case _:
                    self.view.show_message(" Неверный выбор. Попробуйте снова.")
