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
  
  def _create_type(self, row_pos_0, col_pos_0, row_pos_1, col_pos_1, amt, piece, inc):
      """
      Places pieces for both teams in alternating fashion across specified positions.
      
      Args:
          row_pos_0: Starting row position for team 0
          col_pos_0: Starting column position for team 0
          row_pos_1: Starting row position for team 1
          col_pos_1: Starting column position for team 1
          amt: Total number of pieces to place (split evenly between teams)
          piece: Piece class to instantiate
          inc: Column increment value for each placement
      
      Returns:
          None
      """
      for i in range(amt):
          if i % 2 == 0:
              self.board[row_pos_0][col_pos_0] = piece(1)
              col_pos_0 += inc
          else:
              self.board[row_pos_1][col_pos_1] = piece(0)
              col_pos_1 += inc

  def create_pieces(self):
    self._create_type(1, 0, 6, 0, 16, Pawn, 1)
    self._create_type(0, 0, 7, 0, 4, Rook, 7)
    self._create_type(0, 1, 7, 1, 4, Knight, 5)
    self._create_type(0, 2, 7, 2, 4, Bishop, 3)
    self._create_type(0, 3, 7, 3, 2, Queen, 0)
    self._create_type(0, 4, 7, 4, 2, King, 0)
    
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