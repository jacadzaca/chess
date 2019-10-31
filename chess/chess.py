from board import Board
import vector


def main():
    chess_board = Board()
    print(chess_board)
    print(chess_board.get_node_at(vector.parse_vector('01')).piece)
    chess_board.execute_command('06 04')


if __name__ == '__main__':
    main()
