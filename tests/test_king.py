import sys
import unittest
from pathlib import Path

# Add parent directory to Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

from board import Board
from pieces.king import King
from pieces.pawn import Pawn

class TestKing(unittest.TestCase):

    def test_king_all_moves(self):
      """
      Test King from bottom corner
      """
      board = Board()
      current_board = board.get_board
      
      current_board[7][0] = King(1)
      moves = current_board[7][0].get_possible_moves(board, 7, 0)
      
      self.assertIn([6,0], moves)
      self.assertIn([7,1], moves)
      self.assertIn([6,1], moves)
      self.assertEqual(len(moves), 3)

    def test_king_friendly_block_at_end(self):
      """
      Test King from bottom corner, has 3 friendly pieces
      at end of move range
      """
      board = Board()
      current_board = board.get_board
      
      current_board[7][0] = King(1)
      current_board[6][0] = Pawn(1)
      current_board[7][1] = Pawn(1)
      current_board[6][1] = Pawn(1)

      moves = current_board[7][0].get_possible_moves(board, 7, 0)
      
      self.assertEqual(len(moves), 0)

    def test_king_enemey_at_end(self):
      """
      Test King from bottom corner, has 3 enemy pieces
      at end of move range
      """
      board = Board()
      current_board = board.get_board
      
      current_board[7][0] = King(1)
      current_board[6][0] = Pawn(0)
      current_board[7][1] = Pawn(0)
      current_board[6][1] = Pawn(0)

      moves = current_board[7][0].get_possible_moves(board, 7, 0)
      
      self.assertEqual(len(moves), 3)

    def test_king_mid_field_open(self):
      """
      A mid field test to make sure King gets
      all moves in every direction.
      """

      board = Board()
      current_board = board.get_board
      
      current_board[4][3] = King(1)

      moves = current_board[4][3].get_possible_moves(board, 4, 3)

      self.assertIn([3,2], moves)
      self.assertIn([5,3], moves)
      self.assertIn([4,2], moves)
      self.assertIn([4,4], moves)
      self.assertIn([5,2], moves)
      self.assertIn([3,4], moves)
      self.assertIn([5,3], moves)
      self.assertIn([3,3], moves)

      self.assertEqual(len(moves), 8)





