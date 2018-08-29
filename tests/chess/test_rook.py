from chess.rook import Rook
from chess.chessboard import Chessboard
from chess.game import Game


def test_legal_move():
    # this is a dummy test for the dummy implementation
    cb = Chessboard(Game.WHITE_PIECES, Game.BLACK_PIECES)
    p = Rook(0, 0, "W", "WR1")
    assert p.is_legal_move([1, 1], cb.status()) == True