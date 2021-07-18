from random import shuffle

from .roles import Civilian, Mafia, Officer
from .gamer import Gamer

roles_by_number_of_gamers = {4: [Mafia, Civilian, Civilian, Civilian],
                             5: [Mafia, Mafia, Civilian, Civilian, Civilian],
                             6: [Mafia, Mafia, Civilian, Civilian, Civilian, Civilian],
                             7: [Mafia, Mafia, Officer, Civilian, Civilian, Civilian, Civilian]}


class Game:

    def __init__(self, chat_id, source_id, name):
        self.gamers = [Gamer(source_id, name)]
        self.chat_id = chat_id
        self.votes = {}
        self.count_of_mafia = 0
        self.mafia_votes = {}
        self.is_day = True
        self.is_game_started = False

    @staticmethod
    def gather_players():
        return 'Игра создана, присоединяйтесь!'

    def gather_player(self, source_id, name):
        if any(map(lambda gamer: gamer.name == name, self.gamers)):
            return 'Вы уже зарегестрированы!'
        self.gamers.append(Gamer(source_id, name))
        message = f'В игру вошел {name}. Количество игроков на данный момент: {len(self.gamers)}.'
        if len(self.gamers) == 7:
            return message + '\n\n' + self.start(), True
        elif 4 < len(self.gamers) < 7:
            return message + ' Вы можете начать игру!', False
        return message, False

    def start(self):
        if len(self.gamers) in roles_by_number_of_gamers.keys():
            roles = roles_by_number_of_gamers[len(self.gamers)].copy()
            shuffle(roles)
            for gamer in self.gamers:
                gamer.set_role(roles.pop()(self))
            self.is_day = False
            self.make_turn()
            self.is_game_started = True
            return 'Город засыпает, просыпается мафия и знакомится друг с другом'
        else:
            return 'Игроков должно быть от 4 до 7'

    def end(self, winner):
        return f"Игра закончена! Победили {winner} "

    def kick(self, voting):
        new_gamers = []
        person_name = max(voting.items(), key=lambda x: x[1])[0]
        person = None
        for gamer in self.gamers:
            if gamer.name == person_name:
                person = gamer
            else:
                new_gamers.append(gamer)
        self.gamers = new_gamers
        if isinstance(person.role, Mafia):
            self.count_of_mafia -= 1
        if self.count_of_mafia < 1:
            self.end('мирные жители')
            return
        elif len(self.gamers) - self.count_of_mafia < 2:
            self.end('мафиози')
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
        if not self.is_day:
            return "Наступает ночь. Мафия выбирает свою жертву."
        elif self.is_day:
            return "Наступает день. Жители начинают голосование."
