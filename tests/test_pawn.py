import sys
import unittest
from pathlib import Path

# Add parent directory to Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

from board import Board
from pieces.pawn import Pawn


class TestPawn(unittest.TestCase):

    def test_white_pawn_attack_right_and_left(self):
        """
        White pawn should have two diagonal attacks against black pawns.
        """
        board = Board()
        
        current_board = board.get_board
        
        current_board[3][3] = Pawn(1)
        current_board[4][2] = Pawn(0)
        current_board[4][4] = Pawn(0) 
        current_board[4][3] = Pawn(1)
        
        moves = current_board[3][3].get_possible_moves(board, 3, 3)
        
        self.assertIn([4, 2], moves)  
        self.assertIn([4, 4], moves)  
        self.assertEqual(len(moves), 2)

    def test_black_pawn_attack_right_and_left(self):
        board = Board()
        
        current_board = board.get_board
        
        current_board[4][4] = Pawn(0)  
        current_board[3][3] = Pawn(1)   
        current_board[3][5] = Pawn(1)  
        current_board[3][4] = Pawn(0)  
        
        moves = current_board[4][4].get_possible_moves(board, 4, 4)
        
        self.assertIn([3, 3], moves) 
        self.assertIn([3, 5], moves) 
        self.assertEqual(len(moves), 2)

    def test_white_pawn_side_attacks_blocked_center_open(self):
            board = Board()
            
            current_board = board.get_board
            
            current_board[4][3] = Pawn(1)  
            current_board[5][2] = Pawn(1)  
            current_board[5][4] = Pawn(1)  
            
            moves = current_board[4][3].get_possible_moves(board, 4, 3)
            
            self.assertIn([5, 3], moves)
            self.assertIn([6, 3], moves)
            self.assertEqual(len(moves), 2)

