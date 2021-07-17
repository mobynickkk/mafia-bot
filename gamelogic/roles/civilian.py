from gamelogic.roles.abstractRole import AbstractRole


class Civilian(AbstractRole):
    literal = 'Мирный житель'

    def do_step(self):
        return 'Ночью вы можете только спать :('
