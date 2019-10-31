from vector import Vector


class Pawn():
    def __init__(self, owner):
        self._owner = owner
        self._already_moved = False

    def is_legal_move(self, move_vector):
        if not self._already_moved:
            return move_vector == Vector(0, 1) or move_vector == Vector(0, 2)
        return move_vector == Vector(0, 1)

    def is_legal_attack(self, attack_vector):
        return attack_vector == Vector(1, 1) or attack_vector == Vector(-1, 1)

    @property
    def owner(self):
        return self._owner

    def __str__(self):
        return 'P'
