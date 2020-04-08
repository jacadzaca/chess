from vector import Vector
from pieces.piece_properties import PieceProperties


class King(PieceProperties):
    def __init__(self, owner):
        super().__init__(owner, 'K', is_king=True)

    def is_legal_move(self, move):
        return (move == Vector(0, 1)
                or move == Vector(0, -1)
                or move == Vector(1, 0)
                or move == Vector(-1, 0))

    def is_legal_attack(self, attack):
        return self.is_legal_move(attack)
