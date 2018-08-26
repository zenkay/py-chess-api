from flask import Flask, render_template
app = Flask(__name__)

from chess.chessboard import Chessboard

CHESS_ICONS = {
    "BK": "&#9818;",
    "BQ": "&#9819;",
    "BR": "&#9820;",
    "BB": "&#9821;",
    "BN": "&#9822;",
    "BP": "&#9823;",
    "WK": "&#9812;",
    "WQ": "&#9813;",
    "WR": "&#9814;",
    "WB": "&#9815;",
    "WN": "&#9816;",
    "WP": "&#9817;"
}

cb = Chessboard()

def toggle_color(i, j):
    if ((i * 8) + j + i) % 2 == 0:
        return "white"
    return "black"

def resolve_piece(label):
    if len(label) != 3:
        return ""
    return CHESS_ICONS[label[0:2]]

@app.route("/", methods=['GET'])
def welcome():
    return render_template('welcome.html')

@app.route("/move", methods=['GET'])
def move():
    cb.attempt_move('BP1', 'A6')
    return "Move a Piece on the Chessboard"

@app.route("/status", methods=['GET'])
def status():
    chessboard = cb.status()
    return render_template('status.html', cb=chessboard, toggle=toggle_color, resolve=resolve_piece)

@app.route("/restart", methods=['POST'])
def restart():
    return "Reset the chessboard and restart the game"
