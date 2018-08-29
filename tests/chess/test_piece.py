from chess.piece import Piece
from chess.chessboard import Chessboard
from chess.game import Game


def test_take_piece():
    p = Piece(0, 0, "W", "WB1")
    assert p.is_taken() == False
    p.set_as_taken()
    assert p.is_taken() == True
    assert p.rank == -1
    assert p.file == -1

def test_update_position():
    p = Piece(0, 1, "W", "WB1")
    assert p.rank == 0
    assert p.file == 1
    p.update_position(3, 4)
    assert p.rank == 3
    assert p.file == 4