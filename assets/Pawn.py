from assets.Piece import Piece

class Pawn(Piece):
    def __init__(self, pos, color):
        self.symbol = 'P' if(color) else 'p'
        super().__init__(pos, color)

    def findMoves(self):
        if self.color:
            self.possibleMoves.append( [self.pos[0] - 1, self.pos[1]] )
            if self.pos[0] == 6:
                self.possibleMoves.append( [self.pos[0] - 2, self.pos[1]] )
        else:
            self.possibleMoves.append( [self.pos[0] + 1, self.pos[1]] )
            if self.pos[0] == 1:
                self.possibleMoves.append( [self.pos[0] + 2, self.pos[1]] )
