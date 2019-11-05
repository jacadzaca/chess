from vector import Vector


class Pawn():
    def __init__(self, owner, board):
        self._owner = owner
        self._already_moved = False
        self._board = board

    def is_legal_move(self, position, desired_position):
        move = desired_position - position
        predicate = move == Vector(0, 1)
        if not self._already_moved:
            predicate = move == Vector(0, 1) or move == Vector(0, 2)
        is_legal_attack = predicate and self._board.are_all_tiles_on_move_empty(position, desired_position, move)
        if is_legal_attack:
            self._already_moved = True
        return is_legal_attack

    def is_legal_attack(self, position, desired_position):
        attack = desired_position - position
        return attack == Vector(1, 1) and self._board.are_all_tiles_on_move_empty_except_last(position, desired_position, attack)

    @property
    def owner(self):
        return self._owner

    def __str__(self):
        return 'P'
