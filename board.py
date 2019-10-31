from tile import Tile
from pieces.pawn import Pawn
import vector

_BLACK = 0
_WHITE = 1


class Board:
    def __init__(self):
        self._tiles = []
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

    def get_node_at(self, positon):
        return self._tiles[positon.y][positon.x]

    def execute_command(self, command):
        '''command is a string of format [digitdigit digitdigit].
        Example: "00 01" '''
        tiles = command.split(' ')
        current_position = vector.parse_vector(tiles[0])
        desired_position = vector.parse_vector(tiles[1])
        move = current_position - desired_position
        current_tile = self.get_node_at(current_position)
        desired_tile = self.get_node_at(desired_position)
        if current_tile.piece.is_legal_move(move) and not desired_tile.is_occupied():
            pass

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
