from vector import Vector


class Knight:
    def __init__(self, owner):
        self._owner = owner

    def is_legal_move(self, move_vector):
        return move_vector == Vector(1, 2)

    def is_legal_attack(self, attack_vector):
        return self.is_legal_move(attack_vector)

    @property
    def is_jumper(self):
        return True

    @property
    def owner(self):
        return self._owner

    def __str__(self):
        return 'K'
