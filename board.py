from tile import Tile
from pieces.pawn import Pawn
import vector

_BLACK = 0
_WHITE = 1


class Board:
    def __init__(self):
        self._nodes = []
        for i in range(8):
            self._nodes.append([])
            for j in range(8):
                self._nodes[i].append(Tile())
        self.create_pieces()

    def create_pieces(self):
        black_pawns_row = self._nodes[1]
        for tile in black_pawns_row:
            tile.current_piece = Pawn(_BLACK)
        whie_pawns_row = self._nodes[6]
        for tile in whie_pawns_row:
            tile.current_piece = Pawn(_WHITE)

    def get_node_at(self, positon):
        return self._nodes[positon.y][positon.x]

    def make_move(self, move_command):
        '''move command is a string like format [digitdigit digitdigit].
        Example: "00 01" '''
        tiles = move_command.split(' ')
        current_position = vector.parse_vector(tiles[0])
        desired_position = vector.parse_vector(tiles[1])
        move = current_position - desired_position
        if self.get_node_at(current_position).current_piece.is_legal_move(move) and not self.get_node_at(desired_position).is_occupied():
            pass

    def __str__(self):
        board_representation = '  0 1 2 3 4 5 6 7'
        row_count = -1
        for row in self._nodes:
            row_count += 1
            for i in range(len(row)):
                if i == 0:
                    board_representation += '\n{} '.format(row_count)
                board_representation += '{} '.format(row[i])
        return board_representation
