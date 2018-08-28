from piece import *


class Pawn(Piece):

    def is_legal_move(self, target, chessboard):
        # move
        if target[0] == start[0]-1 and target[1] == start[1]:
            return True
        # capture right
        elif target[0] == start[0]-1 and target[1] == start[1]+1 and chessboard[target[0]][target[1]] != "" and chessboard[target[0]][target[1]][0] != piece_team:
            return True
        # capture left
        elif target[0] == start[0]-1 and target[1] == start[1]-1 and chessboard[target[0]][target[1]] != "" and chessboard[target[0]][target[1]][0] != piece_team:
            return True
        # no other moves
        else:
            return False
