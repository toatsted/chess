from assets.Piece import Piece

class Knight(Piece):
    def __init__(self, pos, color):
        self.symbol = 'N' if(color) else 'n'
        super().__init__(pos, color)

    def findMoves(self):
        y = self.pos[0]
        x = self.pos[1]
        moves = [
                [y - 2, x + 1],
                [y - 2, x - 1],
                [y + 2, x + 1],
                [y + 2, x - 1],
                [y - 1, x + 2],
                [y - 1, x - 2],
                [y + 1, x + 2],
                [y + 1, x - 2]
            ]
        for move in moves:
            if self.checkLegalMove(move):
                self.possibleMoves.append(move)
