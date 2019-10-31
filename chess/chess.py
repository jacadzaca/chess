from board import Board


def main():
    chess_board = Board()
    print(chess_board)
    chess_board.execute_command('06 04')
    print(chess_board)


if __name__ == '__main__':
    main()
