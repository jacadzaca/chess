class PieceProperties():
    def __init__(self, owner, representation, is_jumper=False, is_king=False):
        self._owner = owner
        self._representation = representation
        self._is_jumper = is_jumper
        self._is_king = is_king

    @property
    def is_jumper(self):
        return self._is_jumper

    @property
    def is_kign(self):
        return self._is_kign

    @property
    def owner(self):
        return self._owner

    def __str__(self):
        return self._representation
