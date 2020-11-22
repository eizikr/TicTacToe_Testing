# This file was written by Itzik_Rahamim - 312202351
import unittest
import Tic_Tac_Toe

# This is a test class for Tic_Tac_Toe program
class TestTicTacToe(unittest.TestCase):

    def reset_board(self):
        """This method help us to clean the board so we can check some new cases"""
        Tic_Tac_Toe.board[0][0] = Tic_Tac_Toe.EMPTY
        Tic_Tac_Toe.board[0][1] = Tic_Tac_Toe.EMPTY
        Tic_Tac_Toe.board[0][2] = Tic_Tac_Toe.EMPTY
        Tic_Tac_Toe.board[1][0] = Tic_Tac_Toe.EMPTY
        Tic_Tac_Toe.board[1][1] = Tic_Tac_Toe.EMPTY
        Tic_Tac_Toe.board[1][2] = Tic_Tac_Toe.EMPTY
        Tic_Tac_Toe.board[2][0] = Tic_Tac_Toe.EMPTY
        Tic_Tac_Toe.board[2][1] = Tic_Tac_Toe.EMPTY
        Tic_Tac_Toe.board[2][2] = Tic_Tac_Toe.EMPTY

    def test_is_valid_move(self):
        """This function returns true when two first values we sent are
            between 0 to 2, and if this spot is not empty"""
        # Clean board
        self.reset_board()

        # Check valid values
        self.assertTrue(Tic_Tac_Toe.is_valid_move(0, 0, Tic_Tac_Toe.CROSS))
        self.assertTrue(Tic_Tac_Toe.is_valid_move(0, 1, Tic_Tac_Toe.CIRCLE))
        self.assertTrue(Tic_Tac_Toe.is_valid_move(0, 2, Tic_Tac_Toe.CROSS))
        self.assertTrue(Tic_Tac_Toe.is_valid_move(1, 0, Tic_Tac_Toe.CIRCLE))
        self.assertTrue(Tic_Tac_Toe.is_valid_move(1, 1, Tic_Tac_Toe.CROSS))
        self.assertTrue(Tic_Tac_Toe.is_valid_move(1, 2, Tic_Tac_Toe.CIRCLE))
        self.assertTrue(Tic_Tac_Toe.is_valid_move(2, 0, Tic_Tac_Toe.CROSS))
        self.assertTrue(Tic_Tac_Toe.is_valid_move(2, 1, Tic_Tac_Toe.CIRCLE))
        self.assertTrue(Tic_Tac_Toe.is_valid_move(2, 2, Tic_Tac_Toe.CROSS))

        # Check negative values
        self.assertFalse(Tic_Tac_Toe.is_valid_move(1, -1, Tic_Tac_Toe.CROSS))
        self.assertFalse(Tic_Tac_Toe.is_valid_move(-1, 1, Tic_Tac_Toe.CIRCLE))

        # Check value is bigger then 2
        self.assertFalse(Tic_Tac_Toe.is_valid_move(1, 3, Tic_Tac_Toe.CROSS))
        self.assertFalse(Tic_Tac_Toe.is_valid_move(3, 1, Tic_Tac_Toe.CIRCLE))

        # Check board-spot isn't empty
        Tic_Tac_Toe.board[1][1] = Tic_Tac_Toe.CROSS
        self.assertFalse(Tic_Tac_Toe.is_valid_move(1, 1, Tic_Tac_Toe.CROSS))
        Tic_Tac_Toe.board[0][1] = Tic_Tac_Toe.CROSS
        self.assertFalse(Tic_Tac_Toe.is_valid_move(0, 1, Tic_Tac_Toe.CIRCLE))

    def test_has_won(self):
        """This method testing a function that returns true or false if player has won
        player wining when ther is a full (3 in line) row, column or diagonal of his sign"""
        # Clean board
        self.reset_board()

        # Check Rows
        Tic_Tac_Toe.board[0][0] = Tic_Tac_Toe.CROSS
        Tic_Tac_Toe.board[0][1] = Tic_Tac_Toe.CROSS
        Tic_Tac_Toe.board[0][2] = Tic_Tac_Toe.CROSS
        self.assertTrue(Tic_Tac_Toe.has_won(Tic_Tac_Toe.CROSS, 0, 0))
        self.assertTrue(Tic_Tac_Toe.has_won(Tic_Tac_Toe.CROSS, 0, 1))
        self.assertTrue(Tic_Tac_Toe.has_won(Tic_Tac_Toe.CROSS, 0, 2))
            # Change 1 value and check
        Tic_Tac_Toe.board[0][0] = Tic_Tac_Toe.CIRCLE
        self.assertFalse(Tic_Tac_Toe.has_won(Tic_Tac_Toe.CROSS, 0, 0))
        self.assertFalse(Tic_Tac_Toe.has_won(Tic_Tac_Toe.CROSS, 0, 1))
        self.assertFalse(Tic_Tac_Toe.has_won(Tic_Tac_Toe.CROSS, 0, 2))

        # Check diagonal
            # Forward
        self.reset_board()
        Tic_Tac_Toe.board[0][2] = Tic_Tac_Toe.CROSS
        Tic_Tac_Toe.board[1][1] = Tic_Tac_Toe.CROSS
        Tic_Tac_Toe.board[2][0] = Tic_Tac_Toe.CROSS
        self.assertTrue(Tic_Tac_Toe.has_won(Tic_Tac_Toe.CROSS, 0, 0))
        self.assertTrue(Tic_Tac_Toe.has_won(Tic_Tac_Toe.CROSS, 0, 1))
        self.assertTrue(Tic_Tac_Toe.has_won(Tic_Tac_Toe.CROSS, 2, 0))
            # Backward
        self.reset_board()
        Tic_Tac_Toe.board[0][0] = Tic_Tac_Toe.CIRCLE
        Tic_Tac_Toe.board[1][1] = Tic_Tac_Toe.CIRCLE
        Tic_Tac_Toe.board[2][2] = Tic_Tac_Toe.CIRCLE
        self.assertTrue(Tic_Tac_Toe.has_won(Tic_Tac_Toe.CIRCLE, 0, 0))
        self.assertTrue(Tic_Tac_Toe.has_won(Tic_Tac_Toe.CIRCLE, 0, 1))
        self.assertTrue(Tic_Tac_Toe.has_won(Tic_Tac_Toe.CIRCLE, 2, 0))

        # Check Columns
        self.reset_board()
        Tic_Tac_Toe.board[0][1] = Tic_Tac_Toe.CROSS
        Tic_Tac_Toe.board[1][1] = Tic_Tac_Toe.CROSS
        Tic_Tac_Toe.board[2][1] = Tic_Tac_Toe.CROSS
        self.assertTrue(Tic_Tac_Toe.has_won(Tic_Tac_Toe.CROSS, 0, 1))
        self.assertTrue(Tic_Tac_Toe.has_won(Tic_Tac_Toe.CROSS, 1, 1))
        self.assertTrue(Tic_Tac_Toe.has_won(Tic_Tac_Toe.CROSS, 2, 1))
            # Change 1 value and check
        Tic_Tac_Toe.board[2][1] = Tic_Tac_Toe.CIRCLE
        self.assertFalse(Tic_Tac_Toe.has_won(Tic_Tac_Toe.CROSS, 0, 1))
        self.assertFalse(Tic_Tac_Toe.has_won(Tic_Tac_Toe.CROSS, 1, 1))
        self.assertFalse(Tic_Tac_Toe.has_won(Tic_Tac_Toe.CROSS, 2, 1))

    def test_validate_3_in_diagonal(self):
        """This method testing a function that returns true if there is backward or forward diagonal of
        Cross or Circle, using the functions backward_diagonal and forward_diagonal"""
        # Clean board
        self.reset_board()

        # Make backward diagonal and check
        Tic_Tac_Toe.board[0][2] = Tic_Tac_Toe.CROSS
        Tic_Tac_Toe.board[1][1] = Tic_Tac_Toe.CROSS
        Tic_Tac_Toe.board[2][0] = Tic_Tac_Toe.CROSS
        self.assertTrue(Tic_Tac_Toe.validate_3_in_diagonal(Tic_Tac_Toe.CROSS))
        self.assertFalse(Tic_Tac_Toe.validate_3_in_diagonal(Tic_Tac_Toe.CIRCLE))

        # Cancel the middle one and check if false
        Tic_Tac_Toe.board[1][1] = Tic_Tac_Toe.EMPTY
        self.assertFalse(Tic_Tac_Toe.validate_3_in_diagonal(Tic_Tac_Toe.CROSS))

        # Check forward with circle
        self.reset_board()
        Tic_Tac_Toe.board[0][0] = Tic_Tac_Toe.CIRCLE
        Tic_Tac_Toe.board[1][1] = Tic_Tac_Toe.CIRCLE
        Tic_Tac_Toe.board[2][2] = Tic_Tac_Toe.CIRCLE
        self.assertTrue(Tic_Tac_Toe.validate_3_in_diagonal(Tic_Tac_Toe.CIRCLE))
        self.assertFalse(Tic_Tac_Toe.validate_3_in_diagonal(Tic_Tac_Toe.CROSS))

        # Cancel the middle one and check if false
        Tic_Tac_Toe.board[1][1] = Tic_Tac_Toe.EMPTY
        self.assertFalse(Tic_Tac_Toe.validate_3_in_diagonal(Tic_Tac_Toe.CIRCLE))

    def test_backward_diagonal(self):
        """This method testing a function that returns true if
        there is a backward diagonal of Cross or Circle
        for example:
                     X || ||
                     || X ||
                     || || X """
        # Clean board
        self.reset_board()

        # Make a backward diagonal of crosses
        Tic_Tac_Toe.board[0][2] = Tic_Tac_Toe.CROSS
        Tic_Tac_Toe.board[1][1] = Tic_Tac_Toe.CROSS
        Tic_Tac_Toe.board[2][0] = Tic_Tac_Toe.CROSS

        # Check function returns true
        self.assertTrue(Tic_Tac_Toe.backward_diagonal(Tic_Tac_Toe.CROSS))
        self.assertFalse(Tic_Tac_Toe.backward_diagonal(Tic_Tac_Toe.CIRCLE))

        # Cancel diagonal and check if false
        Tic_Tac_Toe.board[0][2] = Tic_Tac_Toe.EMPTY
        self.assertFalse(Tic_Tac_Toe.backward_diagonal(Tic_Tac_Toe.CIRCLE))
        self.assertFalse(Tic_Tac_Toe.backward_diagonal(Tic_Tac_Toe.CROSS))

    def test_forward_diagonal(self):
        """This method testing a function that returns true if
        there is a backward diagonal of Cross or Circle
                for example:
                            || || O
                            || O ||
                            O || ||    """
        # Clean board
        self.reset_board()

        # Make a forward diagonal of circles
        Tic_Tac_Toe.board[0][0] = Tic_Tac_Toe.CIRCLE
        Tic_Tac_Toe.board[1][1] = Tic_Tac_Toe.CIRCLE
        Tic_Tac_Toe.board[2][2] = Tic_Tac_Toe.CIRCLE

        # Check function returns true
        self.assertTrue(Tic_Tac_Toe.forward_diagonal(Tic_Tac_Toe.CIRCLE))
        self.assertFalse(Tic_Tac_Toe.forward_diagonal(Tic_Tac_Toe.CROSS))

        # Cancel diagonal and check if false
        Tic_Tac_Toe.board[1][1] = Tic_Tac_Toe.EMPTY
        self.assertFalse(Tic_Tac_Toe.forward_diagonal(Tic_Tac_Toe.CIRCLE))
        self.assertFalse(Tic_Tac_Toe.forward_diagonal(Tic_Tac_Toe.CROSS))

    def test_validate_3_in_column(self):
        """This method testing a function that returns true if
        there are 3 of Cross or Circle in one column"""
        # Clean board
        self.reset_board()

        # Make column of 3 circles in the first column and check if returns true
        Tic_Tac_Toe.board[0][0] = Tic_Tac_Toe.CIRCLE
        Tic_Tac_Toe.board[1][0] = Tic_Tac_Toe.CIRCLE
        Tic_Tac_Toe.board[2][0] = Tic_Tac_Toe.CIRCLE
        self.assertTrue(Tic_Tac_Toe.validate_3_in_column(0,Tic_Tac_Toe.CIRCLE))

        # Check wrong line
        self.assertFalse(Tic_Tac_Toe.validate_3_in_column(1,Tic_Tac_Toe.CIRCLE))

        # Check wrong sign
        self.assertFalse(Tic_Tac_Toe.validate_3_in_column(0, Tic_Tac_Toe.CROSS))

        # Make column of 3 crosses in the last column and check if results are even
        Tic_Tac_Toe.board[0][2] = Tic_Tac_Toe.CROSS
        Tic_Tac_Toe.board[1][2] = Tic_Tac_Toe.CROSS
        Tic_Tac_Toe.board[2][2] = Tic_Tac_Toe.CROSS
        self.assertEqual(Tic_Tac_Toe.validate_3_in_column(0,Tic_Tac_Toe.CIRCLE),Tic_Tac_Toe.validate_3_in_column(2,Tic_Tac_Toe.CROSS))

    def test_validate_3_in_row(self):
        """This method testing a function that returns true if
        there are 3 of Cross or Circle in one row"""
        # Clean board
        self.reset_board()

        # Make column of 3 crosses in the last row and check if returns true
        Tic_Tac_Toe.board[2][0] = Tic_Tac_Toe.CROSS
        Tic_Tac_Toe.board[2][1] = Tic_Tac_Toe.CROSS
        Tic_Tac_Toe.board[2][2] = Tic_Tac_Toe.CROSS
        self.assertTrue(Tic_Tac_Toe.validate_3_in_row(2,Tic_Tac_Toe.CROSS))

        # Check wrong line
        self.assertFalse(Tic_Tac_Toe.validate_3_in_row(1, Tic_Tac_Toe.CROSS))

        # Check wrong sign
        self.assertFalse(Tic_Tac_Toe.validate_3_in_row(2,Tic_Tac_Toe.CIRCLE))

        # Make row of 3 circles in the first row and check if results are even
        Tic_Tac_Toe.board[0][0] = Tic_Tac_Toe.CIRCLE
        Tic_Tac_Toe.board[0][1] = Tic_Tac_Toe.CIRCLE
        Tic_Tac_Toe.board[0][2] = Tic_Tac_Toe.CIRCLE
        self.assertEqual(Tic_Tac_Toe.validate_3_in_row(2,Tic_Tac_Toe.CROSS),Tic_Tac_Toe.validate_3_in_row(0,Tic_Tac_Toe.CIRCLE))

    def test_is_draw(self):
        """This method will check if 'is draw' function is working as we want"""
        # Fill board (If the board is full its Draw!)
        Tic_Tac_Toe.board[0][0] = Tic_Tac_Toe.CIRCLE
        Tic_Tac_Toe.board[0][1] = Tic_Tac_Toe.CROSS
        Tic_Tac_Toe.board[0][2] = Tic_Tac_Toe.CROSS
        Tic_Tac_Toe.board[1][0] = Tic_Tac_Toe.CROSS
        Tic_Tac_Toe.board[1][1] = Tic_Tac_Toe.CIRCLE
        Tic_Tac_Toe.board[1][2] = Tic_Tac_Toe.CIRCLE
        Tic_Tac_Toe.board[2][0] = Tic_Tac_Toe.CIRCLE
        Tic_Tac_Toe.board[2][1] = Tic_Tac_Toe.CROSS
        Tic_Tac_Toe.board[2][2] = Tic_Tac_Toe.CROSS
        self.assertEqual(Tic_Tac_Toe.is_draw(),True)

        # Clean 1 block
        Tic_Tac_Toe.board[1][2] = Tic_Tac_Toe.EMPTY
        self.assertNotEqual(Tic_Tac_Toe.is_draw(),True)

# Init the game so we can start make tests
Tic_Tac_Toe.init_game()

# Run tests commands
if __name__ == '__main__':
    unittest.main()