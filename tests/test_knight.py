import sys
import unittest
from pathlib import Path

# Add parent directory to Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

from board import Board
from pieces.knight import Knight
from pieces.pawn import Pawn


class TestKnight(unittest.TestCase):

    def test_knight_all_moves(self):
        """
        Knight should have all 8 attacks available, no other pieces
        """
        board = Board()
        current_board = board.get_board
        
        current_board[4][3] = Knight(1)
        moves = current_board[4][3].get_possible_moves(board, 4, 3)
        
        self.assertIn([2,2], moves)
        self.assertIn([2,4], moves)
        self.assertIn([3,1], moves)
        self.assertIn([3,5], moves)
        self.assertIn([5,1], moves)
        self.assertIn([5,5], moves)
        self.assertIn([6,2], moves)
        self.assertIn([6,4], moves)
        self.assertEqual(len(moves), 8)

    def test_knight_no_moves(self):
        """
        Knight should have no moves, friendly pawns blocking
        """
        board = Board()
        current_board = board.get_board

        current_board[4][3] = Knight(1)
        current_board[2][2] = Pawn(1)
        current_board[2][4] = Pawn(1)
        current_board[3][5] = Pawn(1)
        current_board[5][5] = Pawn(1)
        current_board[6][4] = Pawn(1)
        current_board[6][2] = Pawn(1)
        current_board[5][1] = Pawn(1)
        current_board[3][1] = Pawn(1)
        moves = current_board[4][3].get_possible_moves(board, 4, 3)

        self.assertEqual(len(moves), 0)

    def test_knight_all_move_enemy_occupied(self):
        """
        Knight should have all moves, not blocked by enemies
        """
        board = Board()
        current_board = board.get_board

        current_board[4][3] = Knight(1)
        current_board[2][2] = Pawn(0)
        current_board[2][4] = Pawn(0)
        current_board[3][5] = Pawn(0)
        current_board[5][5] = Pawn(0)
        current_board[6][4] = Pawn(0)
        current_board[6][2] = Pawn(0)
        current_board[5][1] = Pawn(0)
        current_board[3][1] = Pawn(0)
        moves = current_board[4][3].get_possible_moves(board, 4, 3)

        self.assertIn([2,2], moves)
        self.assertIn([2,4], moves)
        self.assertIn([3,1], moves)
        self.assertIn([3,5], moves)
        self.assertIn([5,1], moves)
        self.assertIn([5,5], moves)
        self.assertIn([6,2], moves)
        self.assertIn([6,4], moves)
        self.assertEqual(len(moves), 8)
        

        
