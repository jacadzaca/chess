''' this file contains class that is supposed to handle pieces like queen or rooks,
    pieces that can move variable number of fileds in certain directions, i.e move freely '''


class FreelyMovingPiece:
    def __init__(self, owner, representation, allowed_move_directions):
        '''owner is one of the possible value of Player enum,
           representation should be a single character,
           allowed_move_directions should be able to handle in'''
        self._owner = owner
        self._representation = representation
        self._allowed_move_directions = allowed_move_directions

    def is_legal_move(self, move):
        return move.direction() in self._allowed_move_directions

    def is_legal_attack(self, attack):
        return self.is_legal_move(attack)

    @property
    def is_jumper(self):
        return False

    @property
    def owner(self):
        return self._owner

    def __str__(self):
        return self._representation
