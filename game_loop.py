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
  
  #Moving player selects game piece to be moved
  not_valid = True
  while not_valid:  
      
      piece_to_move = None
      while piece_to_move is None:
          
          #Selected goes through input sanitation, validation 
          piece_to_move, msg = Utilities.get_selection()
          if piece_to_move[0] is None or piece_to_move[1] is None:
            print(msg)
            piece_to_move = None

      #Selected piece is validated based on team
      
      info = board.get_pos_information(piece_to_move[1], piece_to_move[0])
      if info["is_occupied"] == False or team_to_color[info["team"]] != team_to_color[turn%2]:
          print("That is not a valid piece to move, please try again")
          not_valid = True
      else:
          not_valid = False
          
          #Get moves based on piece type and location
          current_board = board.get_board
          target = current_board[piece_to_move[1]][piece_to_move[0]]
          moves = target.get_possible_moves(board, piece_to_move[1], piece_to_move[0])
          
          #Get and validate second move location
          pos_to_move_to = None
          while pos_to_move_to is None:
            pos_to_move_to, msg = Utilities.get_selection(True)
            
            print(moves)
            location = []
            location.append(pos_to_move_to[1])
            location.append(pos_to_move_to[0])
            print(location)

            if pos_to_move_to[1] is None or pos_to_move_to[0] is None:
                print(msg)
                pos_to_move_to = None
            
            if location not in moves: 
                print("That is not a valid move")
                pos_to_move_to = None  
  turn += 1


