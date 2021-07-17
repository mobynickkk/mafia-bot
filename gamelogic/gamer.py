from .roles import Civilian


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
