from vector import Vector
import math

SQRT2_OVER_2 = math.sqrt(2) / 2
_ALLOWED_MOVE_DIRECTIONS = [Vector(0, 1), Vector(1, 0), Vector(SQRT2_OVER_2, SQRT2_OVER_2)]


class Queen:
    def __init__(self, owner, board):
        self._owner = owner
        self._board = board

    def is_legal_move(self, move_vector):
        direction = move_vector.direction()
        print('x={}, y={}'.format(direction.x, direction.y))
        print('x={}, y={}'.format(_ALLOWED_MOVE_DIRECTIONS[2].x, _ALLOWED_MOVE_DIRECTIONS[2].y))
        return direction in _ALLOWED_MOVE_DIRECTIONS and self._are_all_tiles_on_move_empty(move_vector)

    def _are_all_tiles_on_move_empty(self, move_vector):
        while move_vector.x != 0 and move_vector.y != 0:
            if move_vector.x != 0:
                move_vector.x -= 1
            if move_vector.y != 0:
                move_vector.y -= 1
            if self._board.get_tile_at(move_vector).is_occupied():
                return False
        return True

    def is_legal_attack(self, attack_vector):
        return attack_vector == Vector(1, 1)

    @property
    def owner(self):
        return self._owner

    def __str__(self):
        return 'Q'
