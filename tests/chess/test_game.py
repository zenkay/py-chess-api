from chess.game import Game


def test_legal_move():
    g = Game()
    is_legal, details = g.is_legal("WP1", "A3")
    assert is_legal == True

def test_illegal_move():
    g = Game()
    is_legal, details = g.is_legal("WP1", "C7")
    assert is_legal == False