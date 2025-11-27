from pieces.pawn import Pawn
from pieces.rook import Rook
from pieces.knight import Knight
from pieces.bishop import Bishop
from pieces.queen import Queen
from pieces.king import King

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
  
  def _create_type(self, team_zero_pos, team_one_pos,  piece, amt, inc):
      """
      Places pieces for both teams in alternating fashion across specified positions.
      
      Args:
          team_zero_pos: int list - [row, col] position for team 1
          team_one_pos: int list - [row, col ] position for team 0
          piece: Piece class to instantiate
          amt: Total number of pieces to place (split evenly between teams)
          inc: Column increment value for each placement
      
      Returns:
          None
      """
      for i in range(amt):
          if i % 2 == 0:
              self.board[team_zero_pos[0]][team_zero_pos[1]] = piece(1)
              team_zero_pos[1] += inc
          else:
              self.board[team_one_pos[0]][team_one_pos[1]] = piece(0)
              team_one_pos[1] += inc

  def create_pieces(self):
    self._create_type([1, 0], [6, 0], Pawn, 16,  1)
    self._create_type([0, 0], [7, 0], Rook, 4,  7)
    self._create_type([0, 1], [7, 1], Knight, 4,  5)
    self._create_type([0, 2], [7, 2], Bishop, 4,  3)
    self._create_type([0, 3], [7, 3], Queen, 2,  0)
    self._create_type([0, 4], [7, 4], King, 2,  0)
    
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
board.clear()
board.create_pieces()
print(board)