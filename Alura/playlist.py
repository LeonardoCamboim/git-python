
class Program:

    def __init__(self, name, year):
        self._name = name.title()
        self.year = year
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def give_like(self):
        self._likes += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_title):
        self._name = new_title.title()

    def __str__(self):
        return f'{self._name} - {self.year} - {self._likes} likes'


class Film(Program):

    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration

    def __str__(self):
        return f'{self._name} - {self.year} - {self.duration} minutos {self._likes} likes'

class Serie(Program):

    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons

    def __str__(self):
        return f'{self._name} - {self.year} - {self.seasons} seasons {self._likes} likes'

class Playlist:

    def __init__(self, name, programs):
        self.name = name.title()
        self._programs = programs

    def __getitem__(self, item):
        return self._programs[item]

    def __len__(self):
        return len(self._programs)

    @property
    def listing(self):
        return self._programs




vingadores = Film('vingadores', 1991, 160)
atlanta = Serie('atlanta', 2018, 2)
demolidor = Serie('demolidor', 2016, 2)
tmep = Film('Todo mundo em panico', 1999, 100)

vingadores.give_like()
vingadores.give_like()
demolidor.give_like()
tmep.give_like()
tmep.give_like()
atlanta.give_like()
atlanta.give_like()

films_and_series = [vingadores, atlanta, demolidor, tmep]

playlist_weekend = Playlist('fim de semana', films_and_series)

print(f'O tamanho da playlist é: {len(playlist_weekend)}')

for program in playlist_weekend:
    print(program)
