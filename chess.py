import sys

import pygame as p
from chess.chess_display import constants as c
from chess.chess_display import utility


pieces = utility.load_pieces(c.PIECE_DIR+"default/")
# squares = utility.load_board_squares(c.SQUARE_DIR+"default/")
gs = [['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
      ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
      ['--', '--', '--', '--', '--', '--', '--', '--'],
      ['--', '--', '--', '--', '--', '--', '--', '--'],
      ['--', '--', '--', '--', '--', '--', '--', '--'],
      ['--', '--', '--', '--', '--', '--', '--', '--'],
      ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
      ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']]


def main():
    p.init()
    screen = p.display.set_mode((c.BOARD_HEIGHT+c.BOARDER*2, c.BOARD_WIDTH+c.BOARDER*2))
    clock = p.time.Clock()
    screen.fill(p.Color("tan"))

    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        clock.tick(c.MAX_FPS)
        p.display.flip()
        draw_squares(screen)
        draw_pieces(screen)


def draw_squares(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for row in range(c.BOARD_DIMENSIONS):
        for col in range(c.BOARD_DIMENSIONS):
            color = colors[((row + col) % 2)]
            p.draw.rect(screen, color, p.Rect(row*c.SQ_SIZE+c.BOARDER, col*c.SQ_SIZE+c.BOARDER, c.SQ_SIZE, c.SQ_SIZE))


def draw_pieces(screen):
    for row in range(c.BOARD_DIMENSIONS):
        for col in range(c.BOARD_DIMENSIONS):
            piece = gs[row][col]
            if piece != '--':
                screen.blit(pieces[piece], p.Rect(col*c.SQ_SIZE+c.BOARDER, row*c.SQ_SIZE+c.BOARDER, c.SQ_SIZE, c.SQ_SIZE))


if __name__ == "__main__":
    main()
