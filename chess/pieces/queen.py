from vector import Vector
import math


class Queen:
    def __init__(self, owner, board):
        self._owner = owner
        self._board = board

    def is_legal_move(self, move):
        return move.direction() in _ALLOWED_MOVE_DIRECTIONS()

    def is_legal_attack(self, attack):
        return attack.direction() in _ALLOWED_MOVE_DIRECTIONS()

    @property
    def is_jumper(self):
        return False

    @property
    def owner(self):
        return self._owner

    def __str__(self):
        return 'Q'


def _ALLOWED_MOVE_DIRECTIONS():
    sqrt2_over_2 = math.sqrt(2) / 2
    return [Vector(0, 1), Vector(1, 0), Vector(sqrt2_over_2, sqrt2_over_2)]
