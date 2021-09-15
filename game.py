import chess

class ChessGame():
    def __init__(self, white, black, maxTurns = 1000):
        self.board = chess.Board()
        self.white = white
        self.black = black
        self.maxTurns = maxTurns

    """
    Play chess with the bots.
    
    Returns:
        0 - Draw = maximum turns reached
        1 - White wins
        -1 - Black wins
    """
    def play(self) -> int:
        while True:
            # TODO: Play whoever's turn it is
            turn = self.board.turn

            # TODO: Check if someone has won
            if self.board.fullmove_number >= self.maxTurns or self.board.is_stalemate():
                return 0
