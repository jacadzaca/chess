import math
import copy
import itertools
from players import Player


class Board:
    def __init__(self, variant_creator):
        self._tiles = variant_creator()
        self._turn = Player.WHITE
        self._width = len(self._tiles[0])

    def get_tile_at(self, positon):
        '''raises IndexError if position is out of board's range'''
        return self._tiles[positon.y][positon.x]

    def execute_attack(self, command):
        '''@param see command.py
           is_valid_attack is expected to be invoked before this method
           it's up to user to change the turn'''
        command.desired_tile.piece = None
        command.desired_tile.piece = command.tile.piece
        command.tile.piece = None

    def execute_move(self, command):
        '''@param see command.py
           is_valid_move is expected to be invoked before this method
           it's up to user to change the turn'''
        command.desired_tile.piece = command.piece
        command.tile.piece = None
        command.piece.already_moved = True

    def is_valid_move(self, command):
        return (self._is_pices_owners_turn(command)
                and command.piece.is_legal_move(command.move)
                and self._is_move_clear(command))

    def change_turn(self):
        if self._turn is Player.WHITE:
            self._turn = Player.BLACK
        elif self._turn is Player.BLACK:
            self._turn = Player.WHITE

    def _is_move_clear(self, command):
        return (command.piece.is_jumper
                and not command.desired_tile.is_occupied()
                or self._are_all_tiles_on_move_empty(command.move,
                                                     command.position,
                                                     command.desired_position))

    def is_valid_attack(self, command):
        if command.desired_tile.piece is None:
            return False
        return (self._is_pices_owners_turn(command)
                and _can_attack_there(command)
                and _are_pices_owners_different(command)
                and self._is_attack_clear(command))

    def _is_pices_owners_turn(self, command):
        return command.piece.owner is self._turn

    def _is_attack_clear(self, command):
        return (command.piece.is_jumper
                or self._are_all_tiles_on_move_empty_except_last(
                    command.move,
                    command.position,
                    command.desired_position))

    def _are_all_tiles_on_move_empty(self, move, position, desired_position):
        temp_position = copy.deepcopy(position)
        while temp_position != desired_position:
            if move.x != 0:
                temp_position.x += int(math.copysign(1, move.x))
            if move.y != 0:
                temp_position.y += int(math.copysign(1, move.y))
            if self.get_tile_at(temp_position).is_occupied():
                return False
        return True

    def _are_all_tiles_on_move_empty_except_last(self,
                                                 move,
                                                 position,
                                                 desired_position):
        temp_desired_positon = copy.deepcopy(desired_position)
        if move.x != 0:
            temp_desired_positon.x -= int(math.copysign(1, move.x))
        if move.y != 0:
            temp_desired_positon.y -= int(math.copysign(1, move.y))
        return self._are_all_tiles_on_move_empty(move,
                                                 position,
                                                 temp_desired_positon)

    def __str__(self):
        board_representation = '  ' + \
            ' '.join(map(str, itertools.takewhile(
                lambda row: row < self._width, itertools.count())))
        for row, row_count in zip(self._tiles, itertools.count()):
            board_representation += '\n' + str(row_count)
            for cell in row:
                board_representation += ' ' + str(cell)
        return board_representation


def _can_attack_there(command):
    return (command.piece.is_legal_attack(command.move)
            and command.desired_tile.is_occupied())


def _are_pices_owners_different(command):
    return command.desired_tile.piece.owner is not command.piece.owner
