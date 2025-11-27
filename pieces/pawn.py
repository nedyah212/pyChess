from pieces._piece import Piece

class Pawn(Piece):

  def __init__(self, team):
    super().__init__(team)
    self.has_moved = False
    self.direction = self.team * -1 
  
  def move(self):
    pass

  def __str__(self):
    return 'P'