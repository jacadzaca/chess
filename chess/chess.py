from board import Board
import vector


def main():
    chess_board = Board(8, 8)
    print(chess_board)
    while True:
        command = parse_command(input())
        chess_board.execute_command(command[0], command[1])
        print(chess_board)


def parse_command(command):
    '''command is a string of format [digitdigit digitdigit].
        Example: "00 01" '''
    tiles = command.split(' ')
    position = vector.parse_vector(tiles[0])
    desired_position = vector.parse_vector(tiles[1])
    return (position, desired_position)


if __name__ == '__main__':
    main()
