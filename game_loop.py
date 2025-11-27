from pieces.pawn import Pawn
from pieces.rook import Rook
from pieces.knight import Knight
from pieces.bishop import Bishop
from pieces.queen import Queen
from pieces.king import King
from board import Board
from utilities import Utilities

game_over = False
board = Board()
board.create_pieces()
team_to_color = {1: "White", 0: "Black"}
turn = 1

while not game_over:
  print(f"\nTurn: {turn}, {team_to_color[turn%2]}'s Turn")
  print(board)
  
  piece_to_move = [None,None]
  while piece_to_move[0] is None: 
    piece_to_move = Utilities.get_selection()
    print(piece_to_move[1])
  info = board.get_pos_information(piece_to_move[0], piece_to_move[1])
  turn += 1



