import collections
import vector

Command = collections.namedtuple('Command', ['position',
                                             'desired_position',
                                             'move',
                                             'piece', 'tile', 'desired_tile'])


def parse_command(command, chess_board):
    '''command is a string of format [digitdigit digitdigit].
        Example: "00 01" '''
    tiles = command.split(' ')
    if len(tiles) != 2:
        raise ValueError
    position = vector.parse_vector(tiles[0])
    desired_position = vector.parse_vector(tiles[1])
    move = desired_position - position
    tile = chess_board.get_tile_at(position)
    desired_tile = chess_board.get_tile_at(desired_position)
    piece = tile.piece
    return Command(position, desired_position, move, piece, tile, desired_tile)
