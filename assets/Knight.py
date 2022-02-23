from assets.Piece import Piece

class Knight(Piece):
    def __init__(self, pos, color):
        self.symbol = 'N' if(color) else 'n'
        super().__init__(pos, color)

    def findMoves(self):
        moves = [
                [self.pos[0] - 2, self.pos[1] + 1],
                [self.pos[0] - 2, self.pos[1] - 1],
                [self.pos[0] + 2, self.pos[1] + 1],
                [self.pos[0] + 2, self.pos[1] - 1],
                [self.pos[0] - 1, self.pos[1] + 2],
                [self.pos[0] - 1, self.pos[1] - 2],
                [self.pos[0] + 1, self.pos[1] + 2],
                [self.pos[0] + 1, self.pos[1] - 2]
            ]
        for move in moves:
            if self.checkLegalMove(move):
                self.possibleMoves.append(move)
