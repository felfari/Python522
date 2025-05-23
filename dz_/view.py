class View:
    @staticmethod
    def show_menu():
        print("\n ===Редактирование данных каталога==="),
        print("1 - Добавление фильма")
        print("2 - Каталог фильмов")
        print("3 - Просмотреть определенного фильма ")
        print("4 - Удалить фильм")
        print("q - Выход из программы ")
        return input("Выберите действие: ")

    @staticmethod
    def show_all(films):
        if not films:
            print("Нет доступных фильмов.")
            return
        print("\nСписок фильмов:")
        for idx, film in enumerate(films, 1):
            print(f"{idx}. {film.title}")

    @staticmethod
    def get_film_details():
        try:
            title = input("Название: ")
            genre = input("Жанр: ")
            director = input("Режиссер: ")
            release_year = int(input("Год выпуска: "))
            duration = int(input("Длительность (мин): "))
            studio = input("Студия: ")
            actors = input("Актеры (через запятую): ").split(',')
            return {
                "title": title,
                "genre": genre,
                "director": director,
                "release_year": release_year,
                "duration": duration,
                "studio": studio,
                "actors": [a.strip() for a in actors]
            }
        except ValueError:
            print("Ошибка: Год и длительность должны быть числами.")
            return None

    @staticmethod
    def show_film(film):
        if film:
            print("\nИнформация о фильме:")
            print(f"Название: {film.title}")
            print(f"Жанр: {film.genre}")
            print(f"Режиссер: {film.director}")
            print(f"Год выпуска: {film.release_year}")
            print(f"Длительность: {film.duration} мин")
            print(f"Студия: {film.studio}")
            print(f"Актеры: {', '.join(film.actors)}")
        else:
            print("Фильм не найден.")

    @staticmethod
    def get_title_input():
        return input("Введите название фильма: ")

    @staticmethod
    def show_message(message):
        print(message)
