import sys
import unittest
from pathlib import Path

# Add parent directory to Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

from board import Board
from pieces.rook import Rook
from pieces.pawn import Pawn

class TestRook(unittest.TestCase):

    def test_rook_all_moves(self):
      """
      Test Rook from bottom corner
      """
      board = Board()
      current_board = board.get_board
      
      current_board[7][0] = Rook(1)
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
      self.assertEqual(len(moves), 14)

    def test_rook_friendly_block_at_end(self):
      """
      Test Rook from bottom corner, has 2 friendly pieces
      at end of move range
      """
      board = Board()
      current_board = board.get_board
      
      current_board[7][0] = Rook(1)
      current_board[0][0] = Pawn(1)
      current_board[7][7] = Pawn(1)
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
      self.assertEqual(len(moves), 12)

    def test_rook_enemey_at_end(self):
      """
      Test Rook from bottom corner, has 2 enemy pieces
      at end of move range
      """
      board = Board()
      current_board = board.get_board
      
      current_board[7][0] = Rook(1)
      current_board[0][0] = Pawn(0)
      current_board[7][7] = Pawn(0)
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
      self.assertEqual(len(moves), 14)

    def test_rook_friendly_block_mid_range(self):
      """
      Test Rook from bottom corner, has 2 friendly pieces
      blocking 3 sqares away
      """
      board = Board()
      current_board = board.get_board
      
      current_board[7][0] = Rook(1)
      current_board[4][0] = Pawn(1)
      current_board[7][3] = Pawn(1)
      moves = current_board[7][0].get_possible_moves(board, 7, 0)
      
      self.assertIn([5,0], moves)
      self.assertIn([6,0], moves)
      self.assertIn([7,1], moves)
      self.assertIn([7,2], moves)
      self.assertEqual(len(moves), 4)

    def test_rook_enemey_mid_range(self):
      """
      Test Rook from bottom corner, has 2 enemy pieces
      at 3 sqares away
      """
      board = Board()
      current_board = board.get_board
      
      current_board[7][0] = Rook(1)
      current_board[4][0] = Pawn(0)
      current_board[7][3] = Pawn(0)
      moves = current_board[7][0].get_possible_moves(board, 7, 0)
      
      self.assertIn([4,0], moves)
      self.assertIn([5,0], moves)
      self.assertIn([6,0], moves)
      self.assertIn([7,1], moves)
      self.assertIn([7,2], moves)
      self.assertIn([7,3], moves)
      self.assertEqual(len(moves), 6)

