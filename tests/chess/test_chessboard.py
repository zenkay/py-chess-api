from chess.chessboard import Chessboard
from chess.game import Game


def test_chessboard_size():
    cb = Chessboard(Game.WHITE_PIECES, Game.BLACK_PIECES)
    assert len(cb.status()) == 8
    for r in cb.status():
        assert len(r) == 8

def test_placed_pieces():
    cb = Chessboard(Game.WHITE_PIECES, Game.BLACK_PIECES)
    pieces_count = 0
    for r in cb.status():
        for f in r:
            if f != "":
                pieces_count += 1
    assert pieces_count == 32
