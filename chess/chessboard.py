WHITE_TEAM = 'W'
WHITE_PIECES = {
    'WP1': [6, 0],
    'WP2': [6, 1],
    'WP3': [6, 2],
    'WP4': [6, 3],
    'WP5': [6, 4],
    'WP6': [6, 5],
    'WP7': [6, 6],
    'WP8': [6, 7],
    'WR1': [7, 0],
    'WN1': [7, 1],
    'WB1': [7, 2],
    'WQ1': [7, 3],
    'WK1': [7, 4],
    'WB2': [7, 5],
    'WN2': [7, 6],
    'WR2': [7, 7]
}
BLACK_TEAM = 'B'
BLACK_PIECES = {
    'BR1': [0, 0],
    'BN1': [0, 1],
    'BB1': [0, 2],
    'BK1': [0, 3],
    'BQ1': [0, 4],
    'BB2': [0, 5],
    'BN2': [0, 6],
    'BR2': [0, 7],
    'BP1': [1, 0],
    'BP2': [1, 1],
    'BP3': [1, 2],
    'BP4': [1, 3],
    'BP5': [1, 4],
    'BP6': [1, 5],
    'BP7': [1, 6],
    'BP8': [1, 7]
}

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

PIECES = WHITE_PIECES.keys() + BLACK_PIECES.keys()

class Chessboard:
    board = None
    next_moving_team = None
    pieces_position = {}
    
    def __init__(self):
        self.init_board()
    
    def _create_board(self):
        self.board = [[""] * 8 for i in xrange(8)]

    def _arrange_pieces(self):
        for k, v in WHITE_PIECES.iteritems():
            self.board[v[0]][v[1]] = k
            self.pieces_position[k] = v
        for k, v in BLACK_PIECES.iteritems():
            self.board[v[0]][v[1]] = k
            self.pieces_position[k] = v

    def init_board(self):
        self.next_moving_team = WHITE_TEAM
        self._create_board()
        self._arrange_pieces()

    def _is_piece_valid(self, label):
        return label in PIECES

    def _is_piece_taken(self, label):
        piece_position = self.pieces_position[label]
        return not (piece_position[0] in range(0, 7) and piece_position[1] in range(0, 7))

    def _is_position_valid(self, position):
        return position[0] in "ABCDEFGH" and position[1] in "12345678"

    def _can_team_move(self, label):
        return self.next_moving_team == label[0]

    def _decode_position(self, position):
        return [RANKS[position[1]], FILES[position[0]]]

    def _get_piece_position(self, label):
        return self.pieces_position[label]

    def _move(self, label, start, target):
        pass

    def attempt_move(self, piece_label, target_position_encoded):
        if(not self._is_position_valid(target_position_encoded)):
            raise Exception("Invalid position on chessboard")
        if(not self._is_piece_valid(piece_label)):
            raise Exception("Invalid piece")
        if(not self._can_team_move(piece_label)):
            raise Exception("Wrong round, wait for your team's round")
        if(self._is_piece_taken(piece_label)):
            raise Exception("Can't move a taken piece")
        
        target_position = self._decode_position(target_position_encoded)
        starting_position = self._get_piece_position(piece_label)

        # piece = create correct piece

        # if(invalid move for piece):
        #     error

        # if(move cross another piece):
        #     error

        # if(another piece taken)
        #     mark the other piece as taken

        self._move(piece_label, starting_position, target_position)

        # update match stats (moving team, ...)
        # check if match ended

    def status(self):
        return self.board

        
