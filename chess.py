WHITE = True
BLACK = False

X = 1
Y = 0

BOARDSIZE = 8


class Board:
    def __init__(self, boardSize):
        self.state = []
        for i in range(boardSize):
            self.state.append('0 0 0 0 0 0 0 0'.split())

    def display(self):
        for row in self.state:
            print(' '.join(row))

    def updatePiece(self, piece):
        self.state[piece.pos[Y]][piece.pos[X]] = piece.symbol
        
class Piece:
    def __init__(self, pos, color):
        # self.pos = [Y, X]
        self.pos = pos
        self.color = color
        self.possibleMoves = []
        board.updatePiece(self)

    def move(self, pos):
        self.pos = pos
        board.updatePiece(self)


class Pawn(Piece):
    def __init__(self, pos, color):
        self.symbol = 'x' if(color) else 'y'
        super().__init__(pos, color)
        self.findMoves()

    def findMoves(self):
        if self.color:
            self.possibleMoves.append( [self.pos[Y] - 1, self.pos[X]] )
            if self.pos[Y] == BOARDSIZE - 2:
                self.possibleMoves.append( [self.pos[Y] - 2, self.pos[X]] )
        else:
            self.possibleMoves.append( [self.pos[Y] + 1, self.pos[X]] )
            if self.pos[Y] == 1:
                self.possibleMoves.append( [self.pos[Y] + 2, self.pos[X]] )


board = Board(BOARDSIZE)

def main():
    p1 = Pawn([BOARDSIZE - 2, 0], WHITE)
    p2 = Pawn([1, 0], BLACK)
    print(p1.possibleMoves)
    print(p2.possibleMoves)

    board.display()

if __name__ == "__main__":
    main()
