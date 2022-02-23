from assets.Board import board

class Piece:
    def __init__(self, pos, color):
        # self.pos = [Y, X]
        self.pos = pos
        self.color = color
        self.possibleMoves = []
        self.move(self.pos)
        self.findMoves()

    def move(self, pos):
        board.state[self.pos[0]][self.pos[1]] = '0'
        self.pos = pos
        board.state[self.pos[0]][self.pos[1]] = self.symbol

    def checkLegalMove(self, move):
        if not move[0] < 0 and not move[0] > 7 and not move[1] < 0 and not move[1] > 7:
            return True
