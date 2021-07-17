from gamelogic.roles.abstractRole import AbstractRole


class Officer(AbstractRole):
    literal = 'Офицер'

    def do_step(self):
        def arrest_person(name):
            if name is None:
                return 'Введите имя подозреваемого'
            self.game.votes[name] = 10
            return f'Вы успешно арестовали {name}'
        return arrest_person
