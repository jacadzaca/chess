from pieces.pawn import Pawn
from pieces.knight import Knight
from pieces.queen import Queen
from players import Player
from tile import Tile
'''this file contains functions that are responsible for creating different chess variants.
    Functions responsible for creating variants are not supposed to take any arguments,
    Functions responsible are suppose to return a board in from of a list of lists,
    It is insited that pieces owners are contained in the Player enum,
    Make sure that the board is a squre (its width is equal to its height)'''


def normal_game():
    tiles = [[Tile() for _ in range(8)] for _ in range(8)]
    black_pawns_row = tiles[1]
    for tile in black_pawns_row:
        tile.piece = Pawn(Player.BLACK)
    whie_pawns_row = tiles[6]
    for tile in whie_pawns_row:
        tile.piece = Pawn(Player.WHITE)
    tiles[0][1].piece = Knight(Player.BLACK)
    tiles[7][1].piece = Knight(Player.WHITE)
    tiles[0][6].piece = Knight(Player.BLACK)
    tiles[7][6].piece = Knight(Player.WHITE)
    tiles[7][4].piece = Queen(Player.WHITE)
    return tiles
