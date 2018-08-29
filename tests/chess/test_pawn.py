from chess.pawn import Pawn
from chess.chessboard import Chessboard
from chess.game import Game


def test_legal_move():
    cb = Chessboard(Game.WHITE_PIECES, Game.BLACK_PIECES)
    p = Pawn(0, 0, "W", "WP1")
    assert p.is_legal_move([1, 1], cb.status()) == True

def test_illegal_move():
    cb = Chessboard(Game.WHITE_PIECES, Game.BLACK_PIECES)
    p = Pawn(0, 0, "W", "WP1")
    assert p.is_legal_move([4, 3], cb.status()) == False