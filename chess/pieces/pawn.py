from vector import Vector


class Pawn():
    def __init__(self, owner, allowed_move_direction):
        self._owner = owner
        self._allowed_move_direction = allowed_move_direction
        self._already_moved = False

    def is_legal_move(self, move):
        predicate = move == Vector(0, 1)
        if not self._already_moved:
            predicate = move == Vector(0, 1) or move == Vector(0, 2)
        return predicate and move.direction().completly_equal(self._allowed_move_direction)

    def is_legal_attack(self, attack):
        return attack == Vector(1, 1)

    @property
    def is_jumper(self):
        return False

    @property
    def owner(self):
        return self._owner

    def __str__(self):
        return 'P'
