from vector import Vector


class King():
    def __init__(self, owner):
        self._owner = owner

    def is_legal_move(self, move):
        return move == Vector(0, 1) or move == Vector(1, 0)

    def is_legal_attack(self, attack):
        return self.is_legal_move(attack)

    @property
    def is_jumper(self):
        return False

    @property
    def owner(self):
        return self._owner

    def __str__(self):
        return 'K'
