from pieces._piece import Piece

class Pawn(Piece):

  def __init__(self, team):
    super().__init__(team)
    self.at_initial_pos = True
    self.direction = self.team * -1
  
  def move(self):
    valid_moves = []
    
  def __str__(self):
    return 'P'