WHITE = True
BLACK = False

class Board:
    def __init__(self, boardSize):
        self.state = []
        for i in range(boardSize):
            self.state.append('0 0 0 0 0'.split())

    def display(self):
        for row in self.state:
            print(' '.join(row))


    def updatePiece(self, piece):
        self.state[piece.pos[0]][piece.pos[1]] = piece.symbol
        

class Piece:
    def __init__(self, pos):
        self.pos = pos
        board.updatePiece(self)

    def move(self, pos):
        self.pos = pos
        board.updatePiece(self)


class O(Piece):
    def __init__(self, pos, color):
        self.symbol = 'x' if(color) else 'y'
        super().__init__(pos)

board = Board(5)

def main():
    o = O([1, 1], WHITE)



    board.display()

if __name__ == "__main__":
    main()
