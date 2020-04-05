from enum import Enum

# https://en.wikipedia.org/wiki/ANSI_escape_code#Colors
_WHITE_ESCAPE_CODE = '97m'
_BLACK_ESCAPE_CODE = '90m'


class Player(Enum):
    """enum containing possible players"""
    WHITE = _WHITE_ESCAPE_CODE
    BLACK = _BLACK_ESCAPE_CODE
