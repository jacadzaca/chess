from tile import Tile
from pieces.pawn import Pawn
from pieces.knight import Knight
from pieces.queen import Queen
import math
import vector
import copy

_BLACK = 0
_WHITE = 1


class Board:
    def __init__(self, width, height):
        self._tiles = [[Tile() for _ in range(width)] for _ in range(height)]
        self.turn = _WHITE
        self.create_pieces()

    def create_pieces(self):
        black_pawns_row = self._tiles[1]
        for tile in black_pawns_row:
            tile.piece = Pawn(_BLACK, self)
        whie_pawns_row = self._tiles[6]
        for tile in whie_pawns_row:
            tile.piece = Pawn(_WHITE, self)
        self._tiles[0][1].piece = Knight(_BLACK)
        self._tiles[7][1].piece = Knight(_WHITE)
        self._tiles[0][6].piece = Knight(_BLACK)
        self._tiles[7][6].piece = Knight(_WHITE)
        self._tiles[7][4].piece = Queen(_WHITE, self)

    def get_tile_at(self, positon):
        return self._tiles[positon.y][positon.x]

    def execute_command(self, command):
        '''command is a string of format [digitdigit digitdigit].
        Example: "00 01" '''
        tiles = command.split(' ')
        position = vector.parse_vector(tiles[0])
        desired_position = vector.parse_vector(tiles[1])
        tile = self.get_tile_at(position)
        desired_tile = self.get_tile_at(desired_position)
        piece = tile.piece
        if piece.owner is self.turn and piece.is_legal_move(copy.deepcopy(position), copy.deepcopy(desired_position)):
            desired_tile.piece = piece
            tile.piece = None
            self.change_turn()
        elif piece.is_legal_attack(position, desired_position) and desired_tile.is_occupied() and desired_tile.piece.owner is not piece.owner:
            desired_tile.piece = None
            desired_tile.piece = piece
            tile.piece = None
            self.change_turn()
        else:
            print('Invalid move command')

    def are_all_tiles_on_move_empty(self, position, desired_position, move):
        while position != desired_position:
            if move.x != 0:
                position.x += int(math.copysign(1, move.x))
            if move.y != 0:
                position.y += int(math.copysign(1, move.y))
            if self.get_tile_at(position).is_occupied():
                return False
        return True

    def are_all_tiles_on_move_empty_except_last(self, position, desired_position, move):
        if move.x != 0:
            desired_position.x -= int(math.copysign(1, move.x))
        if move.y != 0:
            desired_position.y -= int(math.copysign(1, move.y))
        return self.are_all_tiles_on_move_empty(position, desired_position, move)

    def change_turn(self):
        if self.turn is _WHITE:
            self.turn = _BLACK
        elif self.turn is _BLACK:
            self.turn = _WHITE

    def __str__(self):
        board_representation = '  0 1 2 3 4 5 6 7'
        row_count = -1
        for row in self._tiles:
            row_count += 1
            for i in range(len(row)):
                if i == 0:
                    board_representation += '\n{} '.format(row_count)
                board_representation += '{} '.format(row[i])
        return board_representation
