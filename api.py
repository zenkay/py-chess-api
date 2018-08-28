import json
from chess.game import *
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

g = Game()

'''
Main endpoints required for the assignment
'''


@app.route("/move", methods=['GET'])
def move():
    piece = request.args.get('piece').upper()
    target = request.args.get('target').upper()
    try:
        g.move(piece, target)
        return jsonify({"moved": True})
    except Exception as e:
        return jsonify({"moved": False, "details": e.message})


@app.route("/is-legal", methods=['GET'])
def legal():
    piece = request.args.get('piece').upper()
    target = request.args.get('target').upper()
    is_legal, details = g.is_legal(piece, target)
    return jsonify({"is_legal": is_legal, "details": details})


@app.route("/is-taken", methods=['GET'])
def taken():
    piece = request.args.get('piece').upper()
    try:
        return jsonify({"is_taken": g.is_taken(piece)})
    except Exception as e:
        return jsonify({"error": e.message})


'''
Additional endpoints to draw game status
and restart game
'''


@app.route("/", methods=['GET'])
def status():
    chessboard = g.status()
    return render_template('status.html', cb=chessboard, toggle=toggle_color)


@app.route("/restart", methods=['GET'])
def restart():
    return jsonify({"success": True})


'''
Helper methods
'''


def toggle_color(i, j):
    if ((i * 8) + j + i) % 2 == 0:
        return "white"
    return "black"
