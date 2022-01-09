import pygame as p
from chess.chess_display import constants as c


def load_pieces(path):
    pieces = {}
    for piece in c.PIECE_IMAGE_NAMES:
        pieces[piece] = p.transform.scale(p.image.load(path+piece+'.png'), (c.SQ_SIZE, c.SQ_SIZE))
    return pieces


def load_board_squares(path):
    squares = {}
    for square in c.SQUARE_IMAGE_NAMES:
        squares[square] = p.transform.scale(p.image.load(path+square+'.png'), (c.SQ_SIZE, c.SQ_SIZE))
    return squares


def load_clocks():
    pass


def load_side_pane(color):
    pass


def load_border(color):
    pass
