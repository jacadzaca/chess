from vector import Vector
import math


class Queen:
    def __init__(self, owner, board):
        self._owner = owner
        self._board = board

    def is_legal_move(self, current_position, desired_position):
        move_vector = desired_position - current_position
        return move_vector.direction() in _ALLOWED_MOVE_DIRECTIONS() and self._board.are_all_tiles_on_move_empty(current_position, desired_position, move_vector)

    def is_legal_attack(self, current_position, desired_position):
        attack = desired_position - current_position
        return attack.direction() in _ALLOWED_MOVE_DIRECTIONS() and self._board.are_all_tiles_on_move_empty_except_last(current_position, desired_position, attack)

    @property
    def owner(self):
        return self._owner

    def __str__(self):
        return 'Q'


def _ALLOWED_MOVE_DIRECTIONS():
    sqrt2_over_2 = math.sqrt(2) / 2
    return [Vector(0, 1), Vector(1, 0), Vector(sqrt2_over_2, sqrt2_over_2)]
