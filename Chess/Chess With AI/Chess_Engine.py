"""
This class is responsible for storing all the current state of the game. It is also used to determine valid moves.
It will also keep a move log.
"""

class GameState():
    def __init__(self):
        #board is an 8*8 2d list. Each piece has 2 character.
        #First character is the color.
        #Second Character is the Type of Piece.
        #"--" is an empty field.
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]

        self.whiteToMove = True
        self.moveLog = []

    def make_move(self, move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move) #log the move so we can undo it later
        self.whiteToMove = not self.whiteToMove #swap players / switch turns

    """
    Undo the last move
    """
    def undo_move(self):
         pass


class Move():
    #maps keys to values
    #key : value
    ranks_to_rows = {"1":7, "2":6, "3":5, "4":4,
                     "5":3, "6":2, "7":1, "8":0}
    rows_to_ranks = {v: k for k, v in ranks_to_rows.items()}

    files_to_col = {"a": 0, "b": 1, "c": 2, "d": 3,
                    "e": 4, "f": 5, "g": 6, "h": 7}
    col_to_files = {v: k for k, v in files_to_col.items()}

    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]


    def get_chess_notation(self):
        return self.get_rank_file(self.startRow, self.startCol) + self.get_rank_file(self.endRow, self.endCol)

#Sad bhayo

    def get_rank_file(self, r, c):
        return self.col_to_files[c] + self.rows_to_ranks[r]


























