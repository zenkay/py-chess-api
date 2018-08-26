class Piece:
    rank = None # row
    file = None # column
    team = None
    taken = None

    def __init__(self, rank, file, team):
        self.rank = rank
        self.file = file
        self.team = team
        self.taken = False

    def _available_moves(self):
        pass
    
    def _can_move_to(self, destination):
        pass

    def move(self, destination)
        pass
