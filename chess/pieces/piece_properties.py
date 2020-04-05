_SET_COLOR_TERMIANL_COMMAND = '\033['
_RESET_COLOR_TERMINAL_COMMAND = '0m'


class PieceProperties():
    def __init__(self,
                 owner,
                 representation,
                 is_jumper=False, is_king=False, already_moved=False):
        self.owner = owner
        self._representation = (_SET_COLOR_TERMIANL_COMMAND
                                + owner.value
                                + representation
                                + _SET_COLOR_TERMIANL_COMMAND
                                + _RESET_COLOR_TERMINAL_COMMAND)
        self.is_jumper = is_jumper
        self.is_king = is_king
        self.already_moved = already_moved

    def __str__(self):
        return self._representation
