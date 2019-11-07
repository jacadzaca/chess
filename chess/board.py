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
        '''input to this function is expected to be sanitized'''
        move = desired_position - position
        tile = self.get_tile_at(position)
        desired_tile = self.get_tile_at(desired_position)
        piece = tile.piece
        if piece.owner is self._turn and piece.is_legal_move(move) and ((piece.is_jumper and not desired_tile.is_occupied()) or self.are_all_tiles_on_move_empty(position, desired_position, move)):
            desired_tile.piece = piece
            tile.piece = None
            self.change_turn()
        elif piece.is_legal_attack(move) and desired_tile.is_occupied() and desired_tile.piece.owner is not piece.owner and (piece.is_jumper or self.are_all_tiles_on_move_empty_except_last(position, desired_position, move)):
            desired_tile.piece = None
            desired_tile.piece = piece
            tile.piece = None
            self.change_turn()
        else:
            print('Invalid move command')

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
