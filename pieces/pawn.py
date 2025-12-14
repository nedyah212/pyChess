from pieces._piece import Piece

class Pawn(Piece):

  def __init__(self, team):
    super().__init__(team)
    self.at_initial_pos = True
    self.team_to_dir_mult = {1: -1, 0: 1}
    self.direction = self.team_to_dir_mult[self.team] * -1
  
  def get_possible_moves(self, board, yLoc, xLoc):
      moves = []
      board = board.get_board
      
      # Forward move
      if board[yLoc + self.direction][xLoc] == ' ':
          moves.append([yLoc + self.direction, xLoc])
      
          # Double move from starting position
          if self.at_initial_pos:
              if board[yLoc + 2 * self.direction][xLoc] == ' ':
                  moves.append([yLoc + 2 * self.direction, xLoc])
      
      team = self.team
      
      # Diagonal capture right
      if xLoc + 1 <= 7:
        target = board[yLoc + self.direction][xLoc + 1]
        if target != ' ' and target.team != team:
          moves.append([yLoc + self.direction, xLoc + 1])
      
      # Diagonal capture left
      if xLoc - 1 >= 0:
        target = board[yLoc + self.direction][xLoc - 1]
        if target != ' ' and target.team != team:
          moves.append([yLoc + self.direction, xLoc - 1])
      
      return moves
  
  def move(self):
    valid_moves = []
    
  def __str__(self):
    ansi = self.get_ansi()
    return ansi[0] + 'P' + ansi[1]