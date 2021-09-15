import chess

class ChessGame():
    def __init__(self, white, black, maxTurns = 1000):
        self.board = chess.Board()
        self.white = white
        self.black = black
        self.maxTurns = maxTurns

    def play(self):
        pass
