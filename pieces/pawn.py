from pieces._piece import Piece

class Pawn(Piece):

  def __init__(self):
    self.team_to_col = {0: 1, 1: 6}
    self.start_row = self.team_to_col[self.team]

  def move(self):
    pass

  def __str__(self):
    return 'P'