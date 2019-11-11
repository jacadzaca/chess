from board import Board
import variants
import vector


def main():
    chess_board = Board(variants.normal_game)
    print(chess_board)
    while True:
        try:
            command = parse_command(input())
            position = command[0]
            desired_position = command[1]
            tile = chess_board.get_tile_at(position)
            desired_tile = chess_board.get_tile_at(desired_position)
            move = desired_position - position
            piece = tile.piece
            if piece is None:
                print('No pice at that tile')
                print(chess_board)
                continue
            if chess_board.is_valid_move(position, desired_position, move, piece, desired_tile):
                chess_board.execute_move(tile, desired_tile)
                chess_board.change_turn()
            elif chess_board.is_valid_attack(position, desired_position, move, piece, desired_tile):
                chess_board.execute_attack(tile, desired_tile)
                chess_board.change_turn()
            else:
                print('Invalid move command')
        except (ValueError, IndexError):
            print('Cannnot parse the command')
        print(chess_board)


def parse_command(command):
    '''command is a string of format [digitdigit digitdigit].
        Example: "00 01" '''
    tiles = command.split(' ')
    if len(tiles) != 2:
        raise ValueError
    position = vector.parse_vector(tiles[0])
    desired_position = vector.parse_vector(tiles[1])
    return (position, desired_position)


if __name__ == '__main__':
    main()
