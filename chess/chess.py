from board import Board


def main():
    chess_board = Board()
    chess_board.execute_command('06 04')
    chess_board.execute_command('11 13')
    chess_board.execute_command('04 13')
    chess_board.execute_command('01 02')
    chess_board.execute_command('16 15')
    chess_board.execute_command('02 01')
    print(chess_board)


if __name__ == '__main__':
    main()
