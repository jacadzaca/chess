from players import Player
import math
import copy
import itertools


class Board:
    def __init__(self, variant_creator):
        self._tiles = variant_creator()
        self._turn = Player.WHITE
        self._width = len(self._tiles[0])

    def get_tile_at(self, positon):
        return self._tiles[positon.y][positon.x]

    def execute_command(self, position, desired_position):
        '''raises IndexError if position or desired_position is/are out of board's range'''
        move = desired_position - position
        tile = self.get_tile_at(position)
        desired_tile = self.get_tile_at(desired_position)
        piece = tile.piece
        if self.is_valid_move(position, desired_position, move, piece, desired_tile):
            desired_tile.piece = piece
            tile.piece = None
            self.change_turn()
        elif self.is_valid_attack(position, desired_position, move, piece, desired_tile):
            desired_tile.piece = None
            desired_tile.piece = piece
            tile.piece = None
            self.change_turn()
        else:
            print('Invalid move command')

    def is_valid_move(self, position, desired_position, move, piece, desired_tile):
        can_pice_jump = piece.is_jumper and not desired_tile.is_occupied()
        is_move_clear = can_pice_jump or self.are_all_tiles_on_move_empty(position, desired_position, move)
        return piece.owner is self._turn and piece.is_legal_move(move) and is_move_clear

    def is_valid_attack(self, position, desired_position, move, piece, desired_tile):
        move_clear = piece.is_jumper or self.are_all_tiles_on_move_empty_except_last(position, desired_position, move)
        pices_owners_different = desired_tile.piece.owner is not piece.owner
        pices_owners_turn = piece.owner is self._turn
        return pices_owners_turn and piece.is_legal_attack(move) and desired_tile.is_occupied() and pices_owners_different and move_clear

    def are_all_tiles_on_move_empty(self, position, desired_position, move):
        temp_position = copy.deepcopy(position)
        while temp_position != desired_position:
            if move.x != 0:
                temp_position.x += int(math.copysign(1, move.x))
            if move.y != 0:
                temp_position.y += int(math.copysign(1, move.y))
            if self.get_tile_at(temp_position).is_occupied():
                return False
        return True

    def are_all_tiles_on_move_empty_except_last(self, position, desired_position, move):
        temp_desired_positon = copy.deepcopy(desired_position)
        if move.x != 0:
            temp_desired_positon.x -= int(math.copysign(1, move.x))
        if move.y != 0:
            temp_desired_positon.y -= int(math.copysign(1, move.y))
        return self.are_all_tiles_on_move_empty(position, temp_desired_positon, move)

    def change_turn(self):
        if self._turn is Player.WHITE:
            self._turn = Player.BLACK
        elif self._turn is Player.BLACK:
            self._turn = Player.WHITE

    def __str__(self):
        board_representation = '  {}'.format(' '.join(map(str, itertools.takewhile(lambda row: row < self._width, itertools.count()))))
        row_count = -1
        for row in self._tiles:
            row_count += 1
            for i in range(len(row)):
                if i == 0:
                    board_representation += '\n{} '.format(row_count)
                board_representation += '{} '.format(row[i])
        return board_representation
