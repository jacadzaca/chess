from pieces.pawn import Pawn
from pieces.knight import Knight
from pieces.freely_moving_piece import FreelyMovingPiece
from pieces.king import King
from players import Player
from tile import Tile
from vector import Vector
'''this file contains functions that are responsible for creating different chess variants.
    Functions responsible for creating variants are not supposed to take any arguments,
    Functions responsible are suppose to return a board in from of a list of lists,
    It is insited that pieces owners are contained in the Player enum,
    Make sure that the board is a squre (its width is equal to its height)'''


def normal_game():
    tiles = [[Tile() for _ in range(8)] for _ in range(8)]
    black_pawns_row = tiles[1]
    down = Vector(0, 1)
    for tile in black_pawns_row:
        tile.piece = Pawn(Player.BLACK, down)
    whie_pawns_row = tiles[6]
    up = Vector(0, -1)
    for tile in whie_pawns_row:
        tile.piece = Pawn(Player.WHITE, up)
    tiles[0][1].piece = Knight(Player.BLACK)
    tiles[7][1].piece = Knight(Player.WHITE)
    tiles[0][6].piece = Knight(Player.BLACK)
    tiles[7][6].piece = Knight(Player.WHITE)
    sqrt2_over_2 = (2**(1 / 2)) / 2
    left_right_direction = Vector(1, 0)
    up_down_direction = Vector(0, 1)
    all_diagonals = Vector(sqrt2_over_2, sqrt2_over_2)
    queen_allowed_move_directions = [left_right_direction, up_down_direction, all_diagonals]
    tiles[7][3].piece = King(Player.WHITE)
    tiles[0][3].piece = King(Player.BLACK)
    tiles[7][4].piece = FreelyMovingPiece(Player.WHITE, 'Q', queen_allowed_move_directions)
    tiles[0][4].piece = FreelyMovingPiece(Player.BLACK, 'Q', queen_allowed_move_directions)
    tiles[7][2].piece = FreelyMovingPiece(Player.WHITE, 'B', [all_diagonals])
    tiles[7][5].piece = FreelyMovingPiece(Player.WHITE, 'B', [all_diagonals])
    tiles[0][2].piece = FreelyMovingPiece(Player.BLACK, 'B', [all_diagonals])
    tiles[0][5].piece = FreelyMovingPiece(Player.BLACK, 'B', [all_diagonals])
    tiles[7][0].piece = FreelyMovingPiece(Player.WHITE, 'R', [up_down_direction])
    tiles[7][7].piece = FreelyMovingPiece(Player.WHITE, 'R', [up_down_direction])
    tiles[0][0].piece = FreelyMovingPiece(Player.BLACK, 'R', [up_down_direction])
    tiles[0][7].piece = FreelyMovingPiece(Player.BLACK, 'R', [up_down_direction])
    return tiles
