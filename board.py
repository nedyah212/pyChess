from pieces.pawn import Pawn
from pieces.rook import Rook

class Board:

  def __init__(self):
    self.board = self.clear()
    self.position_int_to_char = {
      0: 'a', 1: 'b', 2: 'c', 3: 'd', 
      4: 'e', 5: 'f', 6: 'g', 7: 'h' }
  
  def clear(self):
    board = []
    for r in range(8):
      row = []
      for c in range(8):
        row.append(' ')
      board.append(row)
    return board
  
  def create_pawns(self):
    position_team_zero = 0
    position_team_one = 0
    
    for i in range(16):
      if i % 2 == 0:
        self.board[1][position_team_zero] = Pawn(0)
        position_team_zero += 1        
      else:
        self.board[6][position_team_one] = Pawn(1)
        position_team_one += 1

  def create_rooks(self):
    position_team_zero = 0
    position_team_one = 0

    for i in range(4):
      if i % 2 == 0:
        self.board[0][position_team_zero] = Rook(0)
        position_team_zero += 7
      else:
        self.board[7][position_team_one] = Rook(1)
        position_team_one += 7 

  def create_pieces(self):
    self.create_pawns()
    self.create_rooks()

  def __str__(self):
      result = "\n8 "
      for r in range(7,-1,-1):
          result += "|"
          for c in range(8):
              result += str(self.board[r][c]) + "|" 
          
          if r == 0:
            result += "\n   " 
            for l in range(8):
              result += f"{self.position_int_to_char[l]} "
          else:
            result += f"\n{r} "
      return result


board = Board()
board.create_pieces()
print(board)