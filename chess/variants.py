from pieces.pawn import Pawn
from pieces.knight import Knight
from pieces.freely_moving_piece import FreelyMovingPiece
from pieces.king import King
from players import Player
from tile import Tile
from vector import Vector
'''this file contains functions that
    are responsible for creating different chess variants.
    Functions responsible for creating variants,
    are not supposed to take any arguments,
    Functions responsible for creating variants,
    are suppose to return a board in from of a list of lists,
    It is insited that pieces owners are contained in the Player enum,
    Make sure that the board is a squre (its width is equal to its height)'''


def normal_game():
    tiles = [[Tile() for _ in range(8)] for _ in range(8)]
    sqrt2_over_2 = (2**(1 / 2)) / 2

    black_pawns_row = tiles[1]
    down = Vector(0, 1)
    down_diagonally_right = Vector(sqrt2_over_2, sqrt2_over_2)
    down_diagonally_left = Vector(-sqrt2_over_2, sqrt2_over_2)
    black_pawn_allowed_attack_directions = set(
        [down_diagonally_left, down_diagonally_right])
    _create_pawns(tiles, black_pawns_row, Player.BLACK,
                  down, black_pawn_allowed_attack_directions)

    white_pawns_row = tiles[6]
    up = Vector(0, -1)
    up_diagonally_right = Vector(sqrt2_over_2, -sqrt2_over_2)
    up_diagonally_left = Vector(-sqrt2_over_2, -sqrt2_over_2)
    white_pawn_allowed_attack_directions = set(
        [up_diagonally_right, up_diagonally_left])
    _create_pawns(tiles, white_pawns_row, Player.WHITE,
                  up, white_pawn_allowed_attack_directions)

    _create_knights(tiles)

    right = Vector(1, 0)
    left = Vector(-1, 0)
    queen_allowed_move_directions = set([left,
                                         right,
                                         up,
                                         down,
                                         down_diagonally_left,
                                         down_diagonally_right,
                                         up_diagonally_right,
                                         up_diagonally_left])
    _create_queens(tiles, queen_allowed_move_directions)

    _create_kings(tiles)

    bishop_allowed_move_directions = set([up_diagonally_left,
                                          up_diagonally_right,
                                          down_diagonally_left,
                                          down_diagonally_right])
    _create_bishops(tiles, bishop_allowed_move_directions)

    rook_allowed_move_directions = set([up, down, left, right])
    _create_rooks(tiles, rook_allowed_move_directions)
    return tiles


def _create_pawns(tiles, row, owner,
                  allowed_move_direction, allowed_attack_directions):
    for tile in row:
        tile.piece = Pawn(owner, allowed_move_direction,
                          allowed_attack_directions)


def _create_knights(tiles):
    tiles[0][1].piece = Knight(Player.BLACK)
    tiles[7][1].piece = Knight(Player.WHITE)
    tiles[0][6].piece = Knight(Player.BLACK)
    tiles[7][6].piece = Knight(Player.WHITE)


def _create_queens(tiles, allowed_move_directions):
    tiles[7][4].piece = FreelyMovingPiece(
        Player.WHITE, 'Q', allowed_move_directions)
    tiles[0][4].piece = FreelyMovingPiece(
        Player.BLACK, 'Q', allowed_move_directions)


def _create_kings(tiles):
    tiles[7][3].piece = King(Player.WHITE)
    tiles[0][3].piece = King(Player.BLACK)


def _create_bishops(tiles, allowed_move_directions):
    tiles[7][2].piece = FreelyMovingPiece(
        Player.WHITE, 'B', allowed_move_directions)
    tiles[7][5].piece = FreelyMovingPiece(
        Player.WHITE, 'B', allowed_move_directions)
    tiles[0][2].piece = FreelyMovingPiece(
        Player.BLACK, 'B', allowed_move_directions)
    tiles[0][5].piece = FreelyMovingPiece(
        Player.BLACK, 'B', allowed_move_directions)


def _create_rooks(tiles, allowed_move_directions):
    tiles[7][0].piece = FreelyMovingPiece(
        Player.WHITE, 'R', allowed_move_directions)
    tiles[7][7].piece = FreelyMovingPiece(
        Player.WHITE, 'R', allowed_move_directions)
    tiles[0][0].piece = FreelyMovingPiece(
        Player.BLACK, 'R', allowed_move_directions)
    tiles[0][7].piece = FreelyMovingPiece(
        Player.BLACK, 'R', allowed_move_directions)
