class Tile:
    def __init__(self):
        self._current_piece = None

    def is_occupied(self):
        return self._current_piece is not None

    @property
    def current_piece(self):
        return self._current_piece

    @current_piece.setter
    def current_piece(self, new_piece):
        if self.is_occupied():
            raise RuntimeError('There cannot be two pieces on one tile')
        self._current_piece = new_piece

    def __str__(self):
        if self.is_occupied():
            return str(self.current_piece)
        return '*'
