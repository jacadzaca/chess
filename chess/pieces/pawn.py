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
        move_predicate = (move.length() == Vector(0, 1).length() if self.already_moved
                          else (move.length() == Vector(0, 1).length() or move.length() == Vector(0, 2).length()))
        return (move_predicate
                and move.direction() == self._allowed_move_direction)

    def is_legal_attack(self, attack):
        return (attack.length() == Vector(1, 1).length()
                and attack.direction() in self._allowed_attack_direction)
