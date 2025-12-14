from pieces._piece import Piece

class Queen(Piece):

  def get_possible_moves(self, board, yLoc, xLoc):
    moves = []
    board_state = board.get_board
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    
    for dy, dx in directions:
        for i in range(1, 8):
            newY, newX = yLoc + (dy * i), xLoc + (dx * i)
            
            if not (0 <= newY < 8 and 0 <= newX < 8):
                break
                
            target = board_state[newY][newX]
            
            # Check if it's actually a piece (has team attribute)
            if hasattr(target, 'team'):
                if target.team == self.team:
                    break  # Friendly piece blocks
                else:
                    moves.append([newY, newX])  # Enemy piece - capture
                    break
            else:
                moves.append([newY, newX])  # Empty square - continue
    
    return moves

  def move(self):
    pass

  def __str__(self):
    ansi = self.get_ansi()
    return ansi[0] + 'Q' + ansi[1]