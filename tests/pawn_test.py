# tests/pawn_test.py
import sys
from pathlib import Path

# Add parent directory to Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

from board import Board
from pieces.pawn import Pawn

def test_white_pawn_attack_right_and_left():
    """
    Tests to make sure that a single white pawn has two 
    sideways attacks against a black pawn. Also makes sure 
    that the friendly white pawn in the middle block movement.
    """
    try:
        board = Board()
        current_board = board.get_board
        
        current_board[4][3] = Pawn(1)  # white pawn
        current_board[3][4] = Pawn(0)  # black right
        current_board[3][2] = Pawn(0)  # black left
        current_board[3][3] = Pawn(1)  # white blocker
        
        moves = current_board[4][3].get_possible_moves(board, 4, 3)
        assert [3, 4] in moves
        assert [3, 2] in moves
        assert len(moves) == 2
        print("test #1: test_white_pawn_attack_right_and_left -- passed")
    except AssertionError as e:
        print(f"Test #1 failed: {e}")

def test_black_pawn_attack_right_and_left():
    """
    Tests to make sure that a single black pawn has two 
    sideways attacks against a white pawn. Also makes sure 
    that the friendly black pawn in the middle block movement.
    """
    try:
        board = Board()
        current_board = board.get_board
        
        current_board[3][4] = Pawn(0)  # black pawn
        current_board[4][3] = Pawn(1)  # white right
        current_board[4][5] = Pawn(1)  # white left
        current_board[4][4] = Pawn(0)  # black blocker
        
        moves = current_board[3][4].get_possible_moves(board, 3, 4)
        assert [4, 3] in moves
        assert [4, 5] in moves
        assert len(moves) == 2
        print("test #2: test_black_pawn_attack_right_and_left -- passed")
    except AssertionError as e:
        print(f"Test #2 failed: {e}")

def test_white_pawn_side_attacks_blocked_center_open():
  """
    This test is the opposite of the last one, the flanks are
    blocked by friendly pieces so should not be added, the center
    is left open and should have two moves available.
  """
  try:
    board = Board()
    current_board = board.get_board

    current_board[4][3] = Pawn(1)  # white pawn
    current_board[3][2] = Pawn(1)  # white block
    current_board[3][4] = Pawn(1)  # white block

    moves = current_board[4][3].get_possible_moves(board, 4, 3)

    assert [3, 3] in moves
    assert [2, 3] in moves
    assert len(moves) == 2
    print("test #3: test_white_pawn_side_attacks_blocked_center_open -- passed")

  except AssertionError as e:
    print(f"Test #3 failed: {e}")

def test_black_pawn_side_attacks_blocked_center_open():
    """
    This test is the opposite of the last one, the flanks are
    blocked by friendly pieces so should not be added, the center
    is left open and should have two moves available.
    """
    try:
        board = Board()
        current_board = board.get_board
        
        current_board[3][4] = Pawn(0)  # black pawn
        current_board[4][3] = Pawn(0)  # black block
        current_board[4][5] = Pawn(0)  # black block
        
        moves = current_board[3][4].get_possible_moves(board, 3, 4)
        
        assert [4, 4] in moves
        assert [5, 4] in moves
        assert len(moves) == 2
        
        print("test #4: test_black_pawn_side_attacks_blocked_center_open -- passed")
    except AssertionError as e:
        print(f"Test #4 failed: {e}")

def test_white_pawn_starting_position_four_moves():
    """
    White pawn at starting position (row 6) with diagonal attacks available
    and both forward moves open - should have 4 total moves.
    """
    try:
        board = Board()
        current_board = board.get_board
        current_board[6][3] = Pawn(1)  # white pawn at start
        current_board[5][2] = Pawn(0)  # black pawn left diagonal
        current_board[5][4] = Pawn(0)  # black pawn right diagonal
        moves = current_board[6][3].get_possible_moves(board, 6, 3)
        assert [5, 3] in moves  # one forward
        assert [4, 3] in moves  # two forward
        assert [5, 2] in moves  # attack left
        assert [5, 4] in moves  # attack right
        assert len(moves) == 4
        print("test #5: test_white_pawn_starting_position_four_moves -- passed")
    except AssertionError as e:
        print(f"Test #5 failed: {e}")

def test_black_pawn_starting_position_four_moves():
    """
    Black pawn at starting position (row 1) with diagonal attacks available
    and both forward moves open - should have 4 total moves.
    """
    try:
        board = Board()
        current_board = board.get_board
        current_board[1][4] = Pawn(0)  # black pawn at start
        current_board[2][3] = Pawn(1)  # white pawn left diagonal
        current_board[2][5] = Pawn(1)  # white pawn right diagonal
        moves = current_board[1][4].get_possible_moves(board, 1, 4)
        assert [2, 4] in moves  # one forward
        assert [3, 4] in moves  # two forward
        assert [2, 3] in moves  # attack left
        assert [2, 5] in moves  # attack right
        assert len(moves) == 4
        print("test #6: test_black_pawn_starting_position_four_moves -- passed")
    except AssertionError as e:
        print(f"Test #6 failed: {e}")

test_white_pawn_attack_right_and_left()
test_black_pawn_attack_right_and_left()
test_white_pawn_side_attacks_blocked_center_open()
test_black_pawn_side_attacks_blocked_center_open()
test_white_pawn_starting_position_four_moves()
test_black_pawn_starting_position_four_moves()