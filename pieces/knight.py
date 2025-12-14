from pieces._piece import Piece

class Knight(Piece):

  def get_possible_moves(self, board, yLoc, xLoc):
      moves = []
      delta = [
          [-2, -1], [-2, 1], [-1, -2], [-1, 2], 
          [1, -2], [1, 2], [2, -1], [2, 1]]
      
      board = board.get_board
      i = 0 
      while i <= 7:
          newY = yLoc + delta[i][0]
          newX = xLoc + delta[i][1]
          
          if newY >= 0 and newY <= 7:
              if newX >= 0 and newX <= 7:
                  target = board[newY][newX]
                  if target == ' ' or target.team != self.team:
                      move = [newY, newX]
                      moves.append(move)
          i += 1
      
      return moves

  def __str__(self):
    ansi = self.get_ansi()
    return ansi[0] + 'N' + ansi[1]