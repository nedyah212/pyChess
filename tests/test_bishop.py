import sys
import unittest
from pathlib import Path

# Add parent directory to Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

from board import Board
from pieces.bishop import Bishop
from pieces.pawn import Pawn

class TestBishop(unittest.TestCase):

    def test_bishop_all_moves(self):
      """
      Test Bishop from bottom corner
      """
      board = Board()
      current_board = board.get_board
      
      current_board[7][0] = Bishop(1)
      moves = current_board[7][0].get_possible_moves(board, 7, 0)
      
      self.assertIn([6,1], moves)
      self.assertIn([5,2], moves)
      self.assertIn([4,3], moves)
      self.assertIn([3,4], moves)
      self.assertIn([2,5], moves)
      self.assertIn([1,6], moves)
      self.assertIn([0,7], moves)


      self.assertEqual(len(moves), 7)

    def test_bishop_friendly_block_at_end(self):
      """
      Test Bishop from bottom corner, has 3 friendly pieces
      at end of move range
      """
      board = Board()
      current_board = board.get_board
      
      current_board[7][0] = Bishop(1)
      current_board[0][7] = Pawn(1)

      moves = current_board[7][0].get_possible_moves(board, 7, 0)

      self.assertIn([6,1], moves)
      self.assertIn([5,2], moves)
      self.assertIn([4,3], moves)
      self.assertIn([3,4], moves)
      self.assertIn([2,5], moves)
      self.assertIn([1,6], moves)

      self.assertEqual(len(moves), 6)

    def test_bishop_enemey_at_end(self):
      """
      Test Bishop from bottom corner, has 3 enemy pieces
      at end of move range
      """
      board = Board()
      current_board = board.get_board
      
      current_board[7][0] = Bishop(1)
      current_board[0][7] = Pawn(0)

      moves = current_board[7][0].get_possible_moves(board, 7, 0)

      self.assertIn([6,1], moves)
      self.assertIn([5,2], moves)
      self.assertIn([4,3], moves)
      self.assertIn([3,4], moves)
      self.assertIn([2,5], moves)
      self.assertIn([1,6], moves)
      self.assertIn([0,7], moves)
      
      self.assertEqual(len(moves), 7)

    def test_bishop_friendly_block_mid_range(self):
      """
      Test Bishop from bottom corner, has 3 friendly pieces
      blocking 3 sqares away
      """
      board = Board()
      current_board = board.get_board
      
      current_board[7][0] = Bishop(1)
      current_board[4][3] = Pawn(1)

      moves = current_board[7][0].get_possible_moves(board, 7, 0)
      
      self.assertIn([6,1], moves)
      self.assertIn([5,2], moves)

      self.assertEqual(len(moves), 2)

    def test_bishop_enemey_mid_range(self):
      """
      Test Bishop from bottom corner, has 3 enemy pieces
      at 3 sqares away
      """
      board = Board()
      current_board = board.get_board
      
      current_board[7][0] = Bishop(1)
      current_board[4][3] = Pawn(0)

      moves = current_board[7][0].get_possible_moves(board, 7, 0)
      
      self.assertIn([6,1], moves)
      self.assertIn([5,2], moves)
      self.assertIn([4,3], moves)
      self.assertEqual(len(moves), 3)

    def test_bishop_mid_field_open(self):
      """
      A mid field test to make sure Bishop gets
      all moves in every direction.
      """

      board = Board()
      current_board = board.get_board
      
      current_board[4][3] = Bishop(1)

      moves = current_board[4][3].get_possible_moves(board, 4, 3)

      self.assertIn([1,0], moves)
      self.assertIn([2,1], moves)
      self.assertIn([3,2], moves)

      self.assertIn([0,7], moves)
      self.assertIn([1,6], moves)
      self.assertIn([2,5], moves)
      self.assertIn([3,4], moves)

      self.assertIn([7,6], moves)
      self.assertIn([6,5], moves)
      self.assertIn([5,4], moves)

      self.assertIn([7,0], moves)
      self.assertIn([6,1], moves)
      self.assertIn([5,4], moves)

      self.assertEqual(len(moves), 13)





