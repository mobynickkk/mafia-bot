from random import shuffle

from .roles import Civilian, Mafia, Officer

roles_by_number_of_gamers = {4: [Mafia, Civilian, Civilian, Civilian],
                             5: [Mafia, Mafia, Civilian, Civilian, Civilian],
                             6: [Mafia, Mafia, Civilian, Civilian, Civilian, Civilian],
                             7: [Mafia, Mafia, Officer, Civilian, Civilian, Civilian, Civilian]}


class Gamer:
    def __init__(self, source_id, name):
        self.source_id = source_id
        self.name = name
        self.role = None

    def set_role(self, role):
        self.role = role

    def do_step(self, name=None):
        """ Хендлер для хода игрока в ночное время """
        if not isinstance(self.role, Civilian):
            return self.role.do_step()(name)
        else:
            return self.role.do_step()

    def vote(self, name):
        return self.role.vote(name)


class Game:

    def __init__(self, chat_id, source_id, name):
        self.gamers = [Gamer(source_id, name)]
        self.chat_id = chat_id
        self.votes = {}
        self.count_of_mafia = 0
        self.count_of_nights = 0
        self.mafia_votes = {}
        self.is_day = True

    def start(self):
        if len(self.gamers) in roles_by_number_of_gamers.keys():
            roles = roles_by_number_of_gamers[len(self.gamers)].copy()
            shuffle(roles)
            for gamer in self.gamers:
                gamer.set_role(roles.pop()(self))
            # self.is_day = False
            self.make_turn()
            return 'Город засыпает, просыпается мафия и знакомится друг с другом'
        else:
            return 'Игроков должно быть от 4 до 7'

    def end(self):
        pass

    def kick(self, voting):
        new_gamers = []
        person_name = max(voting.items(), key=lambda x: x[1])[0]
        person = None
        for gamer in self.gamers:
            if gamer.name == person_name:
                person = gamer
            else:
                new_gamers.append(gamer)
        if isinstance(person.role, Mafia):
            self.count_of_mafia -= 1
        if self.count_of_mafia < 1:
            self.end(Mafia)
            return
        elif len(self.gamers) - self.count_of_mafia < 2:
            self.end(Civilian)
            return
        voting.clear()
        return person

    def kick_person_by_voting(self):
        person = self.kick(self.votes)
        return f'{person.name} уехал на шконку. Таких, как он, зовут {person.role.literal}'

    def kick_person_by_mafia_voting(self):
        person = self.kick(self.mafia_votes)
        return f'{person.name} был убит сегодня ночью. Его профессию можно назвать {person.role.literal}'

    def make_turn(self):
        """ """
        # логика ходов, проверка, что мафия сходилась.
        # сделать через потоки (sleep)
        # если день, то проверку, что все проголосовали

        # для ночи
        if not self.is_day:
            pass
        elif self.is_day:
            pass



# в первый день голосуют и в первую ночь убивают