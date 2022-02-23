class Board:
    def __init__(self):
        self.state = []
        self.pieces = {}
        for i in range(8):
            self.state.append('0 0 0 0 0 0 0 0'.split())

    def display(self):
        for row in self.state:
            print(' | '.join(row))
            print('------------------------------')

board = Board()
