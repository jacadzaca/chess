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
        short_move_length = Vector(0, 1).length()
        long_move_length = Vector(0, 2).length()
        move_predicate = (move.length() == short_move_length
                          or move.length() == long_move_length)
        if self.already_moved:
            move_predicate = move.length() == short_move_length
        return (move_predicate
                and move.direction() == self._allowed_move_direction)

    def is_legal_attack(self, attack):
        return (attack.length() == Vector(1, 1).length()
                and attack.direction() in self._allowed_attack_direction)
