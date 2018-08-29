from piece import *


class Pawn(Piece):

    def _1_step_ahead(self, target):
        print("risultato")
        print(target)
        print([self.rank, self.file])
        if self.team == "W":
            return target[0] == self.rank-1\
            and target[1] == self.file
        elif self.team == "B":
            return target[0] == self.rank+1\
            and target[1] == self.file

    def _capture_right(self, target, chessboard):
        if self.team == "W":
            return target[0] == self.rank-1\
            and target[1] == self.file+1\
            and chessboard[target[0]][target[1]] != ""\
            and chessboard[target[0]][target[1]].team != self.team
        elif self.team == "B":
            return target[0] == self.rank-1\
            and target[1] == self.file-1\
            and chessboard[target[0]][target[1]] != ""\
            and chessboard[target[0]][target[1]].team != self.team

    def _capture_left(self, target, chessboard):
        if self.team == "W":
            return target[0] == self.rank+1\
            and target[1] == self.file+1\
            and chessboard[target[0]][target[1]] != ""\
            and chessboard[target[0]][target[1]].team != self.team
        elif self.team == "B":
            return target[0] == self.rank+1\
            and target[1] == self.file-1\
            and chessboard[target[0]][target[1]] != ""\
            and chessboard[target[0]][target[1]].team != self.team

    def _an_passant(self, target, chessboard):
        if self.team == "W":
            return target[0] == self.rank-2\
            and target[1] == self.file\
            and chessboard[self.rank-1][self.file] != ""\
            and chessboard[self.rank-1][self.file].team != self.team
        elif self.team == "B":
            return target[0] == self.rank+1\
            and target[1] == self.file

    def _first_move(self, target, chessboard):
        # Would require to add support for 
        # piece status to detect first move
        # postponed
        pass

    def is_legal_move(self, target, chessboard):
        if self._1_step_ahead(target)\
        or self._capture_right(target, chessboard)\
        or self._capture_left(target, chessboard)\
        or self._an_passant(target, chessboard)\
        or self._an_passant(target, chessboard):
            return True
        return False
