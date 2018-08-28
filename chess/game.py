from chessboard import *
from pawn import *
from bishop import *
from rook import *
from knight import *
from queen import *
from king import *
from piece import *


class Game:

    WHITE_TEAM = 'W'
    WHITE_PIECES = [
        Pawn(6, 0, WHITE_TEAM, 'WP1', Piece.icon("WP")),
        Pawn(6, 1, WHITE_TEAM, 'WP2', Piece.icon("WP")),
        Pawn(6, 2, WHITE_TEAM, 'WP3', Piece.icon("WP")),
        Pawn(6, 3, WHITE_TEAM, 'WP4', Piece.icon("WP")),
        Pawn(6, 4, WHITE_TEAM, 'WP5', Piece.icon("WP")),
        Pawn(6, 5, WHITE_TEAM, 'WP6', Piece.icon("WP")),
        Pawn(6, 6, WHITE_TEAM, 'WP7', Piece.icon("WP")),
        Pawn(6, 7, WHITE_TEAM, 'WP8', Piece.icon("WP")),
        Rook(7, 0, WHITE_TEAM, 'WR1', Piece.icon("WR")),
        Knight(7, 1, WHITE_TEAM, 'WN1', Piece.icon("WN")),
        Bishop(7, 2, WHITE_TEAM, 'WB1', Piece.icon("WB")),
        Queen(7, 3, WHITE_TEAM, 'WQ1', Piece.icon("WQ")),
        King(7, 4, WHITE_TEAM, 'WK1', Piece.icon("WK")),
        Bishop(7, 5, WHITE_TEAM, 'WB2', Piece.icon("WB")),
        Knight(7, 6, WHITE_TEAM, 'WN2', Piece.icon("WN")),
        Rook(7, 7, WHITE_TEAM, 'WR2', Piece.icon("WR"))
    ]

    BLACK_TEAM = 'B'
    BLACK_PIECES = [
        Rook(0, 0, BLACK_TEAM, 'BR1', Piece.icon("BR")),
        Knight(0, 1, BLACK_TEAM, 'BN1', Piece.icon("BN")),
        Bishop(0, 2, BLACK_TEAM, 'BB1', Piece.icon("BB")),
        King(0, 3, BLACK_TEAM, 'BK1', Piece.icon("BK")),
        Queen(0, 4, BLACK_TEAM, 'BQ1', Piece.icon("BQ")),
        Bishop(0, 5, BLACK_TEAM, 'BB2', Piece.icon("BB")),
        Knight(0, 6, BLACK_TEAM, 'BN2', Piece.icon("BN")),
        Rook(0, 7, BLACK_TEAM, 'BR2', Piece.icon("BR")),
        Pawn(1, 0, BLACK_TEAM, 'BP1', Piece.icon("BP")),
        Pawn(1, 1, BLACK_TEAM, 'BP2', Piece.icon("BP")),
        Pawn(1, 2, BLACK_TEAM, 'BP3', Piece.icon("BP")),
        Pawn(1, 3, BLACK_TEAM, 'BP4', Piece.icon("BP")),
        Pawn(1, 4, BLACK_TEAM, 'BP5', Piece.icon("BP")),
        Pawn(1, 5, BLACK_TEAM, 'BP6', Piece.icon("BP")),
        Pawn(1, 6, BLACK_TEAM, 'BP7', Piece.icon("BP")),
        Pawn(1, 7, BLACK_TEAM, 'BP8', Piece.icon("BP"))
    ]

    PIECES = WHITE_PIECES + BLACK_PIECES

    def __init__(self):
        self.setup()

    def setup(self):
        self.board = Chessboard(self.WHITE_PIECES, self.BLACK_PIECES)
        self.next_moving_team = self.WHITE_TEAM

    def _is_piece_valid(self, label):
        return label in self.board.pieces_position.keys()

    def _get_piece_position(self, label):
        piece = self._get_piece(label)
        return [piece.rank, piece.file]

    def _is_position_valid(self, position):
        return position[0] in "ABCDEFGH" and position[1] in "12345678"

    def _can_team_move(self, label):
        return self.next_moving_team == label[0]

    def _decode_position(self, position):
        return [Chessboard.RANKS[position[1]], Chessboard.FILES[position[0]]]

    def _get_piece(self, label):
        return self.board.pieces_position[label]

    def _switch_round(self):
        if self.next_moving_team == self.WHITE_TEAM:
            self.next_moving_team = self.BLACK_TEAM
        else:
            self.next_moving_team = self.WHITE_TEAM

    def _is_capture(self, label, target):
        pass

    def is_legal(self, piece_label, target_position_encoded):
        if(not self._is_position_valid(target_position_encoded)):
            return False, "Invalid position on chessboard"

        if(not self._can_team_move(piece_label)):
            return False, "Wrong round, wait for your team's round"
        
        target_position = self._decode_position(target_position_encoded)
        starting_position = self._get_piece_position(piece_label)

        if target_position == starting_position:
            return False, "Starting position and target position are the same"

        piece = self._get_piece(piece_label)
        
        if(piece.is_taken()):
            return False, "Can't move a taken piece"

        if(not piece.is_legal_move(target_position, self.board)):
            return False, "Invalid move for piece"

        return True, "Valid move"

    def move(self, piece_label, target_position_encoded):
        
        legal, details = self.is_legal(piece_label, target_position_encoded)
        if(legal):

            piece = self._get_piece(piece_label)
            target_position = self._decode_position(target_position_encoded)
            starting_position = self._get_piece_position(piece_label)

            if(self._is_capture(piece, target_position)):
                self._take_piece(target_position)

            self.board.leave_square(starting_position)
            self.board.fill_square(target_position, piece)

            self._switch_round()
        else:
            raise Exception(details)
    
    def is_taken(self, piece_label):
        if(self._is_piece_valid(piece_label)):
            piece = self._get_piece(piece_label)
            return piece.is_taken()
        else:
            raise Exception("Invalid piece")

    def status(self):
        return self.board.status()

        
