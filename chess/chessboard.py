class Chessboard():

    RANKS = {
        "8": 0,
        "7": 1,
        "6": 2,
        "5": 3,
        "4": 4,
        "3": 5,
        "2": 6,
        "1": 7 
    }

    FILES = {
        "A": 0,
        "B": 1,
        "C": 2,
        "D": 3,
        "E": 4,
        "F": 5,
        "G": 6,
        "H": 7     
    }

    def __init__(self, white_pieces, black_pieces):
        self.init_board(white_pieces, black_pieces)

    def _create_board(self):
        self.board = [[""] * 8 for i in xrange(8)]

    def _arrange_pieces(self, white_pieces, black_pieces):
        self.pieces_position = {}
        for piece in white_pieces:
            self.board[piece.rank][piece.file] = piece
            self.pieces_position[piece.label] = piece
        for piece in black_pieces:
            self.board[piece.rank][piece.file] = piece
            self.pieces_position[piece.label] = piece

    def init_board(self, white_pieces, black_pieces):
        self._create_board()
        self._arrange_pieces(white_pieces, black_pieces)

    def leave_square(self, starting):
        self.board[starting[0]][starting[1]] = ""

    def fill_square(self, target, piece):
        print(piece.label)
        self.board[target[0]][target[1]] = piece

    def status(self):
        return self.board