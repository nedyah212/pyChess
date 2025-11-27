from pieces.pawn import Pawn
from pieces.rook import Rook
from pieces.knight import Knight
from pieces.bishop import Bishop
from pieces.queen import Queen
from pieces.king import King
from board import Board

game_over = False
board = Board()
board.create_pieces()
team_to_color = {1: "White", 0: "Black"}
turn = 1

while not game_over:
  print(f"\nTurn: {turn}, {team_to_color[turn%2]}'s Turn")
  print(board)
  selection = input("\nEnter a piece to move: ")
  turn += 1

