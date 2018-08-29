# Chess API

## Requirements

Sketching a simple API for the game of Chess able to:

- enable the user to move pieces on the chessboard
- check whether the move is legal
- deal with possible illegal moves
- check whether a piece is taken

Focus on the interfaces to model the system and the implementation for the rules associated to one of the pieces and for the chessboard. 

## Implementation

Software is designed on 3 key classes: Game, Chessboard and Piece.

- **Game** handles all the features related to game setup and mechanics and answers to the requests from the API.
- **Chessboard** handle the status of the chessboard. Place all the piaces on their initial position and expose methods to move them around.
- **Piece** knows its position, its team and its status. Each subclass (Paws, Rook, Knight, Bishop, King and Queen) has a custom implementation of the method that evaluate if a move is legal.

The API expose 3 endpoint:

POST `/move` to move a piece in a give position (if the move is legal). 
Takes 2 arguments: 
- `piece` the label of the piece to move
- `target` the location where to move the piece (with standard notation)

```
curl -d "piece=WP1&target=A6" -X POST http://127.0.0.1:5000/move
```

GET `/is-legal` to check if a move is legal or not
Takes 2 arguments: 
- `piece` the label of the piece to move
- `target` the location where to move the piece (with standard notation)

```
curl -X GET http://127.0.0.1:5000/is-legal?piece=WP1&target=A6
```

GET `/is-taken` to check if a piece is taken
Takes 1 argument: 
- `piece` the label of the piece to move

```
curl -X GET http://127.0.0.1:5000/is-taken?piece=BK1
```

The API also offer more endpoint
- `/restart` restart the game by resetting the chessboard and the places 
- `/` draw the status of the chessboard with icons of pieces and their acronyms

![chessboard](https://user-images.githubusercontent.com/223858/44769240-45be9f80-ab64-11e8-93d3-96f516c7869b.png)

Pieces are described by a label:
- W or B for the team
- K, Q, B, N, R and P (N is for kNight) for the pieces
- 1 to 8 to identify different pieces of the same type.

Examples:
- White King: WK1
- Black Queen: BQ1
- Last White Pawn: WP8
- Second Black Knight: BN2

Position use the standard notation with files (columns, from A to H) and ranks (rows, from 1 to 8). Chessboard space goes from A1 to H8.

## Development

The project is written using Python (target version is 2.7) and uses Flask to expose the APIs and pytest is used for testing.

To install required library use:

```
pip install -r requirements.txt
```

To run a development server with live reload use:

```
FLASK_DEBUG=1 FLASK_APP=api.py python -m flask run
```

To run tests use

```
python -m pytest tests
```

## References

- https://en.wikipedia.org/wiki/Chess
- http://scacchi.qnet.it/manuale/regole.htm#Indice