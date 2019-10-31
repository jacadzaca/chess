class Tile:
    def __init__(self):
        self._piece = None

    def is_occupied(self):
        return self._piece is not None

    @property
    def piece(self):
        return self._piece

    @piece.setter
    def piece(self, new_piece):
        if self.is_occupied() and new_piece is not None:
            raise RuntimeError('There cannot be two pieces on one tile')
        self._piece = new_piece

    def __str__(self):
        if self.is_occupied():
            return str(self.piece)
        return '*'
