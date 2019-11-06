from board import Board


def main():
    chess_board = Board(8, 8)
    print(chess_board)
    while True:
        command = input()
        chess_board.execute_command(command[0], command[1])
        print(chess_board)


if __name__ == '__main__':
    main()
