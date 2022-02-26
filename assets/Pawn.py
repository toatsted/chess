from assets.Piece import Piece

class Pawn(Piece):
    def __init__(self, pos, color):
        self.symbol = 'P' if(color) else 'p'
        super().__init__(pos, color)

    def findMoves(self):
        whiteMoves = [
                    [self.pos[0] - 1, self.pos[1]],
                    [self.pos[0] - 2, self.pos[1]]
                ]
        blackMoves = [
                    [self.pos[0] + 1, self.pos[1]],
                    [self.pos[0] + 2, self.pos[1]]
                ]


        if self.color:
            if self.checkLegalMove(whiteMoves[0]):
                self.possibleMoves.append(whiteMoves[0])
                if self.pos[0] == 6:
                    if self.checkLegalMove(whiteMoves[1]):
                        self.possibleMoves.append(whiteMoves[1])
        else:
            if self.checkLegalMove(blackMoves[0]):
                self.possibleMoves.append(blackMoves[0])
                if self.pos[0] == 1:
                    if self.checkLegalMove(blackMoves[1]):
                        self.possibleMoves.append(blackMoves[1])
