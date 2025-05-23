import os.path

class Film:
    def __init__(self, title, genre, director, release_year, duration, studio, actors):
        self.title = title
        self.genre = genre
        self.director = director
        self.release_year = release_year
        self.duration = duration
        self.studio = studio
        self.actors = actors

    def to_string(self):

        return f"{self.title}|{self.genre}|{self.director}|{self.release_year}|{self.duration}|{self.studio}|{','.join(self.actors)}"

    @staticmethod
    def from_string(line):

        parts = line.strip().split('|')
        if len(parts) != 7:
            return None
        title, genre, director, release_year, duration, studio, actors_str = parts
        try:
            release_year = int(release_year)
            duration = int(duration)
            actors = actors_str.split(',')
        except ValueError:
            return None
        return Film(title, genre, director, release_year, duration, studio, actors)


class Model:
    def __init__(self):
        self.filename = 'db.txt'
        self.films = self._load()

    def _load(self):
        films_dict = {}
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as f:
                for line in f:
                    film = Film.from_string(line)
                    if film:
                        films_dict[film.title] = film
        return films_dict

    def save(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            for film in self.films.values():
                f.write(film.to_string() + '\n')

    def add_film(self, film_data):
        film = Film(**film_data)
        self.films[film.title] = film
        self.save()

    def get_all_films(self):
        return list(self.films.values())

    def get_film(self, title):
        return self.films.get(title)

    def delete_film(self, title):
        if title in self.films:
            del self.films[title]
            self.save()
            return True
        return False
