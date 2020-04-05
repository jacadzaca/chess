''' FreelyMovingPiece is supposed to handle pieces like queen or rooks,
    pieces that can move variable number of fileds in certain directions,
    i.e move freely'''
from pieces.piece_properties import PieceProperties


class FreelyMovingPiece(PieceProperties):
    def __init__(self, owner, representation, allowed_move_directions):
        '''owner is one of the possible value of Player enum,
           representation should be a single character,
           allowed_move_directions should be able to handle in'''
        super().__init__(owner, representation)
        self._allowed_move_directions = allowed_move_directions

    def is_legal_move(self, move):
        return move.direction() in self._allowed_move_directions

    def is_legal_attack(self, attack):
        return self.is_legal_move(attack)
