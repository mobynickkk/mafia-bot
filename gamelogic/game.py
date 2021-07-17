roles_by_number_of_gamers = {4: ['Мафия', 'Житель', 'Житель', 'Житель'],
                             5: ['Мафия', 'Мафия', 'Житель', 'Житель', 'Житель'],
                             6: ['Мафия', 'Мафия', 'Житель', 'Житель', 'Житель', 'Житель'],
                             7: ['Мафия', 'Мафия', 'Офицер', 'Житель', 'Житель', 'Житель', 'Житель']}


class Gamer:
    def __init__(self, source_id):
        self.source_id = source_id


class Game:
    gamers = []
    roles = {}

    def __init__(self, chat_id, source_id):
        self.chat_id = chat_id
        self.gamers.append(Gamer(source_id))

    def start(self):
        if len(self.gamers) in roles_by_number_of_gamers.keys():
            pass
        else:
            return 'Игроков должно быть от 4 до 7'
