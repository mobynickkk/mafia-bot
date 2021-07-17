from gamelogic.roles.abstractRole import AbstractRole


class Mafia(AbstractRole):
    literal = 'Мафия'

    def do_step(self):
        def kill_person(name):
            if name is None:
                return 'Введите имя своей жертвы'
            self.game.mafia_votes[name] = self.game.mafia_votes.get(name, 0) + 1
            return f'Вы успешно проголосовали за {name}'
        return kill_person
