from pieces._piece import Piece
from pieces.pawn import Pawn
from pieces.rook import Rook
from pieces.knight import Knight
from pieces.bishop import Bishop
from pieces.queen import Queen
from pieces.king import King

class Board:

  @property
  def get_board(self):
    return self._board

  def set_board(self, board):
    self._board = board

  def __init__(self):
    self._board = self.clear()
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
  
  def _create_type(self, black_pos, white_pos,  piece, amount, increment):
      """
      Places pieces for both teams in alternating fashion across specified positions.
      
      Args:
          black_pos: int list - [row, col] position for team 1
          white_pos: int list - [row, col ] position for team 0
          piece: Piece class to instantiate
          amt: Total number of pieces to place (split evenly between teams)
          inc: Column increment value for each placement
      
      Returns:
          None
      """
      for i in range(amount):
          if i % 2 == 1:
              self._board[black_pos[0]][black_pos[1]] = piece(0)
              black_pos[1] += increment
          else:
              self._board[white_pos[0]][white_pos[1]] = piece(1)
              white_pos[1] += increment

  def create_pieces(self):
      self._create_type([6, 0], [1, 0], Pawn, 16, 1) 
      self._create_type([7, 0], [0, 0], Rook, 4, 7) 
      self._create_type([7, 1], [0, 1], Knight, 4, 5)
      self._create_type([7, 2], [0, 2], Bishop, 4, 3)
      self._create_type([7, 3], [0, 3], Queen, 2, 0)
      self._create_type([7, 4], [0, 4], King, 2, 0)   
  
  def get_pos_information(self, yPos, xPos):
    """
    Determines whether a position is occupied and by what color/type of piece.

    Args:
        yPos: integer representing row on board
        xPos: integer representing column on board

    Returns:
        Dict: bool, is_occupied, int team, piece_type Piece 
    """
    
    information = {"is_occupied": False, "team": None, "piece_type": None}
    target = self._board[yPos][xPos]

    if isinstance(target, Piece):
      information["is_occupied"] = True
      information["team"] = target.team
      information["piece_type"] = type(target).__name__

    return information

  def __str__(self):
      result = "\n8 "
      for r in range(7,-1,-1):
          result += "|"
          for c in range(8):
              result += str(self._board[r][c]) + "|" 
          
          if r == 0:
            result += "\n   " 
            for l in range(8):
              result += f"{self.position_int_to_char[l]} "
          else:
            result += f"\n{r} "
      return result
