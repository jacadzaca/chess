from vector import Vector
import math


class Queen:
    def __init__(self, owner, board):
        self._owner = owner
        self._board = board

    def is_legal_move(self, move_vector):
        return move_vector.direction() in _ALLOWED_MOVE_DIRECTIONS()

    def is_piece_moveable_there(self, current_position, move_vector):
        return self._are_all_tiles_on_move_empty(current_position, move_vector)

    def _are_all_tiles_on_move_empty(self, current_position, move_vector):
        desired_position = current_position + move_vector
        while current_position != desired_position:
            if move_vector.x != 0:
                current_position.x += int(math.copysign(1, move_vector.x))
            if move_vector.y != 0:
                current_position.y += int(math.copysign(1, move_vector.y))
            if self._board.get_tile_at(current_position).is_occupied():
                return False
        return True

    def is_legal_attack(self, attack_vector):
        return attack_vector == Vector(1, 1)

    @property
    def owner(self):
        return self._owner

    def __str__(self):
        return 'Q'


def _ALLOWED_MOVE_DIRECTIONS():
    sqrt2_over_2 = math.sqrt(2) / 2
    return [Vector(0, 1), Vector(1, 0), Vector(sqrt2_over_2, sqrt2_over_2)]
