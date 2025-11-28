from pieces.pawn import Pawn
from pieces.rook import Rook
from pieces.knight import Knight
from pieces.bishop import Bishop
from pieces.queen import Queen
from pieces.king import King
from board import Board
from utilities import Utilities

#setup game
game_over = False
board = Board()
board.create_pieces()
team_to_color = {1: "White", 0: "Black"}
turn = 1

#start game loop 
while not game_over:
  print(f"\nTurn: {turn}, {team_to_color[turn%2]}'s Turn")
  print(board)
  
  #Get/validate piece to move
  not_valid = True
  while not_valid:  
      piece_to_move = [None, None]
      while piece_to_move[0] is None: 
          piece_to_move = Utilities.get_selection()
          print(type(piece_to_move))
          print(isinstance(piece_to_move, str))
          if (isinstance(piece_to_move, str)):
            print(piece_to_move)
            selection = None

      info = board.get_pos_information(piece_to_move[0], piece_to_move[1])
      if info["is_occupied"] == False or team_to_color[info["team"]] != team_to_color[turn%2]:
          not_valid = True
      else:
          not_valid = False

  turn += 1



