class AbstractRole:
    literal = 'abstractRole'

    def __init__(self, game):
        self.game = game

    def do_step(self):
        """ Функция для логики ночных ходов """
        raise NotImplemented()

    def vote(self, name):
        """ Функция для логики голосования """
        if name in map(lambda gamer: gamer.get_name(), self.game.gamers):
            self.game.votes[name] = self.game.votes.get(name, 0) + 1
            return f'Голос за игрока {name} принят'
        else:
            return f'Игрок {name} не найден'
