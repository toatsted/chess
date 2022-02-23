from assets.Board import Board, board
from assets.Piece import Piece
from assets.Pawn import Pawn
from assets.Knight import Knight

WHITE = True
BLACK = False

def main():
    board.pieces['P1'] = Pawn([6, 0], WHITE)
    board.pieces['P2'] = Pawn([6, 1], WHITE)
    board.pieces['P3'] = Pawn([6, 2], WHITE)
    board.pieces['P4'] = Pawn([6, 3], WHITE)
    board.pieces['P5'] = Pawn([6, 4], WHITE)
    board.pieces['P6'] = Pawn([6, 5], WHITE)
    board.pieces['P7'] = Pawn([6, 6], WHITE)
    board.pieces['P8'] = Pawn([6, 7], WHITE)
    board.pieces['N1'] = Knight([7, 2], WHITE)
    board.pieces['N2'] = Knight([7, 5], WHITE)

    board.pieces['p1'] = Pawn([1, 0], BLACK)
    board.pieces['p2'] = Pawn([1, 1], BLACK)
    board.pieces['p3'] = Pawn([1, 2], BLACK)
    board.pieces['p4'] = Pawn([1, 3], BLACK)
    board.pieces['p5'] = Pawn([1, 4], BLACK)
    board.pieces['p6'] = Pawn([1, 5], BLACK)
    board.pieces['p7'] = Pawn([1, 6], BLACK)
    board.pieces['p8'] = Pawn([1, 7], BLACK)
    board.pieces['n1'] = Knight([0, 2], BLACK)
    board.pieces['n2'] = Knight([0, 5], BLACK)

    board.display()

if __name__ == "__main__":
    main()
