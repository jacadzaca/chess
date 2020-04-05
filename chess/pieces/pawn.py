from vector import Vector
from pieces.piece_properties import PieceProperties


class Pawn(PieceProperties):
    def __init__(self, owner,
                 allowed_move_direction,
                 allowed_attack_direction):
        super().__init__(owner, 'P')
        self._allowed_move_direction = allowed_move_direction
        self._allowed_attack_direction = allowed_attack_direction

    def is_legal_move(self, move):
        predicate = move == Vector(0, 1)
        if not self.already_moved:
            predicate = move == Vector(0, 1) or move == Vector(0, 2)
        return (predicate
                and move.direction().completly_equal(
                    self._allowed_move_direction))

    def is_legal_attack(self, attack):
        return (attack == Vector(1, 1)
                and self._allowed_attack_direction.y_equal_completly(
                    attack.direction()))
