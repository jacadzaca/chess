from tile import Tile
from pieces.pawn import Pawn
from pieces.knight import Knight
from pieces.queen import Queen
import vector

_BLACK = 0
_WHITE = 1


class Board:
    def __init__(self):
        self._tiles = []
        self.turn = _WHITE
        for i in range(8):
            self._tiles.append([])
            for j in range(8):
                self._tiles[i].append(Tile())
        self.create_pieces()

    def create_pieces(self):
        black_pawns_row = self._tiles[1]
        for tile in black_pawns_row:
            tile.piece = Pawn(_BLACK)
        whie_pawns_row = self._tiles[6]
        for tile in whie_pawns_row:
            tile.piece = Pawn(_WHITE)
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
        current_position = vector.parse_vector(tiles[0])
        desired_position = vector.parse_vector(tiles[1])
        move = desired_position - current_position
        current_tile = self.get_tile_at(current_position)
        desired_tile = self.get_tile_at(desired_position)
        if current_tile.piece.owner is self.turn and current_tile.piece.is_legal_move(move) and current_tile.piece.is_piece_moveable_there(current_position, move):
            desired_tile.piece = current_tile.piece
            current_tile.piece = None
            self.change_turn()
        elif current_tile.piece.is_legal_attack(move) and desired_tile.is_occupied() and desired_tile.piece.owner != current_tile.piece.owner:
            desired_tile.piece = None
            desired_tile.piece = current_tile.piece
            current_tile.piece = None
            self.change_turn()
        else:
            print('Invalid move command')

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
