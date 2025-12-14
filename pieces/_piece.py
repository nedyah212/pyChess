class Piece:

  def __init__(self, team):
    self.team = team

  def get_possible_moves(self, yLoc, xLoc):
    pass

  def get_ansi(self):
    return ("\033[32m", "\033[0m") if self.team == 0 else ("\033[31m", "\033[0m")

  def __str__(self):
    pass