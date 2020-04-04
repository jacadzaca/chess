#!/usr/bin/python3
from board import Board
import variants
import command


def main():
    chess_board = Board(variants.normal_game)
    print(chess_board)
    while True:
        try:
            inputted_command = command.parse_command(input(), chess_board)
            if inputted_command.piece is None:
                print('No pice at that tile')
                print(chess_board)
                continue
            if chess_board.is_valid_move(inputted_command):
                chess_board.execute_move(inputted_command)
                chess_board.change_turn()
            elif chess_board.is_valid_attack(inputted_command):
                chess_board.execute_attack(inputted_command)
                chess_board.change_turn()
            else:
                print('Invalid move command')
        except (ValueError, IndexError):
            print('Cannnot parse the command')
        print(chess_board)


if __name__ == '__main__':
    main()
