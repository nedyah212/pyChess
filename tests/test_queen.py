import sys
import unittest
from pathlib import Path

# Add parent directory to Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

from board import Board
from pieces.queen import Queen
from pieces.pawn import Pawn

class TestQueen(unittest.TestCase):

    def test_queen_all_moves(self):
      """
      Test Queen from bottom corner
      """
      board = Board()
      current_board = board.get_board
      
      current_board[7][0] = Queen(1)
      moves = current_board[7][0].get_possible_moves(board, 7, 0)
      
      self.assertIn([0,0], moves)
      self.assertIn([1,0], moves)
      self.assertIn([2,0], moves)
      self.assertIn([3,0], moves)
      self.assertIn([4,0], moves)
      self.assertIn([5,0], moves)
      self.assertIn([6,0], moves)

      self.assertIn([7,1], moves)
      self.assertIn([7,2], moves)
      self.assertIn([7,3], moves)
      self.assertIn([7,4], moves)
      self.assertIn([7,5], moves)
      self.assertIn([7,6], moves)
      self.assertIn([7,7], moves)

      self.assertIn([6,1], moves)
      self.assertIn([5,2], moves)
      self.assertIn([4,3], moves)
      self.assertIn([3,4], moves)
      self.assertIn([2,5], moves)
      self.assertIn([1,6], moves)
      self.assertIn([0,7], moves)


      self.assertEqual(len(moves), 21)

    def test_queen_friendly_block_at_end(self):
      """
      Test Queen from bottom corner, has 3 friendly pieces
      at end of move range
      """
      board = Board()
      current_board = board.get_board
      
      current_board[7][0] = Queen(1)
      current_board[0][0] = Pawn(1)
      current_board[7][7] = Pawn(1)
      current_board[0][7] = Pawn(1)

      moves = current_board[7][0].get_possible_moves(board, 7, 0)
      
      self.assertIn([1,0], moves)
      self.assertIn([2,0], moves)
      self.assertIn([3,0], moves)
      self.assertIn([4,0], moves)
      self.assertIn([5,0], moves)
      self.assertIn([6,0], moves)

      self.assertIn([7,1], moves)
      self.assertIn([7,2], moves)
      self.assertIn([7,3], moves)
      self.assertIn([7,4], moves)
      self.assertIn([7,5], moves)
      self.assertIn([7,6], moves)

      self.assertIn([6,1], moves)
      self.assertIn([5,2], moves)
      self.assertIn([4,3], moves)
      self.assertIn([3,4], moves)
      self.assertIn([2,5], moves)
      self.assertIn([1,6], moves)

      self.assertEqual(len(moves), 18)

    def test_queen_enemey_at_end(self):
      """
      Test Queen from bottom corner, has 3 enemy pieces
      at end of move range
      """
      board = Board()
      current_board = board.get_board
      
      current_board[7][0] = Queen(1)
      current_board[0][0] = Pawn(0)
      current_board[7][7] = Pawn(0)
      current_board[0][7] = Pawn(0)

      moves = current_board[7][0].get_possible_moves(board, 7, 0)
      
      self.assertIn([0,0], moves)
      self.assertIn([1,0], moves)
      self.assertIn([2,0], moves)
      self.assertIn([3,0], moves)
      self.assertIn([4,0], moves)
      self.assertIn([5,0], moves)
      self.assertIn([6,0], moves)

      self.assertIn([7,1], moves)
      self.assertIn([7,2], moves)
      self.assertIn([7,3], moves)
      self.assertIn([7,4], moves)
      self.assertIn([7,5], moves)
      self.assertIn([7,6], moves)
      self.assertIn([7,7], moves)

      self.assertIn([6,1], moves)
      self.assertIn([5,2], moves)
      self.assertIn([4,3], moves)
      self.assertIn([3,4], moves)
      self.assertIn([2,5], moves)
      self.assertIn([1,6], moves)
      self.assertIn([0,7], moves)
      
      self.assertEqual(len(moves), 21)

    def test_queen_friendly_block_mid_range(self):
      """
      Test Queen from bottom corner, has 3 friendly pieces
      blocking 3 sqares away
      """
      board = Board()
      current_board = board.get_board
      
      current_board[7][0] = Queen(1)
      current_board[4][0] = Pawn(1)
      current_board[7][3] = Pawn(1)
      current_board[4][3] = Pawn(1)

      moves = current_board[7][0].get_possible_moves(board, 7, 0)
      
      self.assertIn([5,0], moves)
      self.assertIn([6,0], moves)    
      self.assertIn([7,1], moves)
      self.assertIn([7,2], moves)
      self.assertIn([6,1], moves)
      self.assertIn([5,2], moves)

      self.assertEqual(len(moves), 6)

    def test_queen_enemey_mid_range(self):
      """
      Test Queen from bottom corner, has 3 enemy pieces
      at 3 sqares away
      """
      board = Board()
      current_board = board.get_board
      
      current_board[7][0] = Queen(1)
      current_board[4][0] = Pawn(0)
      current_board[7][3] = Pawn(0)
      current_board[4][3] = Pawn(0)

      moves = current_board[7][0].get_possible_moves(board, 7, 0)
      
      self.assertIn([4,0], moves)
      self.assertIn([5,0], moves)
      self.assertIn([6,0], moves)
      self.assertIn([7,1], moves)
      self.assertIn([7,2], moves)
      self.assertIn([7,3], moves)
      self.assertIn([6,1], moves)
      self.assertIn([5,2], moves)
      self.assertIn([4,3], moves)
      self.assertEqual(len(moves), 9)

    def test_queen_mid_field_open(self):
      """
      A mid field test to make sure Queen gets
      all moves in every direction.
      """

      board = Board()
      current_board = board.get_board
      
      current_board[4][3] = Queen(1)

      moves = current_board[4][3].get_possible_moves(board, 4, 3)

      self.assertIn([4,0], moves)
      self.assertIn([4,1], moves)
      self.assertIn([4,2], moves)

      self.assertIn([1,0], moves)
      self.assertIn([2,1], moves)
      self.assertIn([3,2], moves)

      self.assertIn([0,3], moves)
      self.assertIn([1,3], moves)
      self.assertIn([2,3], moves)
      self.assertIn([3,3], moves)

      self.assertIn([0,7], moves)
      self.assertIn([1,6], moves)
      self.assertIn([2,5], moves)
      self.assertIn([3,4], moves)

      self.assertIn([4,7], moves)
      self.assertIn([4,6], moves)
      self.assertIn([4,5], moves)
      self.assertIn([4,4], moves)

      self.assertIn([7,6], moves)
      self.assertIn([6,5], moves)
      self.assertIn([5,4], moves)

      self.assertIn([7,3], moves)
      self.assertIn([6,3], moves)
      self.assertIn([5,3], moves)

      self.assertIn([7,0], moves)
      self.assertIn([6,1], moves)
      self.assertIn([5,4], moves)

      self.assertEqual(len(moves), 27)





