class Piece:
    def __init__(self, representation, owner, move_logic):
        self._representation = representation
        self._owner = owner
        self._move_logic = move_logic

    def is_move_possible(self, move):
        return self._move_logic.is_legal_move(move)

    @property
    def owner(self):
        return self._owner

    def __str__(self):
        return self._representation
