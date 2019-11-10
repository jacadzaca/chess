from board import Board
import variants
import vector


def main():
    chess_board = Board(variants.normal_game)
    print(chess_board)
    while True:
        try:
            command = parse_command(input())
            chess_board.execute_command(command[0], command[1])
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
