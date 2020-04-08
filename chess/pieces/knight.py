from pieces.piece_properties import PieceProperties


class Knight(PieceProperties):
    def __init__(self, owner):
        super().__init__(owner, 'K', is_jumper=True)

    def is_legal_move(self, move_vector):
        return (abs(move_vector.x) == 1
                and abs(move_vector.y) == 2)

    def is_legal_attack(self, attack_vector):
        return self.is_legal_move(attack_vector)
