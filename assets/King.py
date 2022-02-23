from assets.Piece import Piece

class King(Piece):
    def __init__(self, pos, color):
        self.symbol = 'K' if(color) else 'k'
        super().__init__(pos,color)

    def findMoves(self):
        y = self.pos[0]
        x = self.pos[1]
        moves = [
                [y + 1, x],
                [y + 1, x + 1],
                [y , x + 1],
                [y - 1, x + 1],
                [y - 1, x],
                [y - 1, x - 1],
                [y, x - 1],
                [y + 1, x - 1],
            ]
        for move in moves:
            if self.checkLegalMove(move):
                self.possibleMoves.append(move)
