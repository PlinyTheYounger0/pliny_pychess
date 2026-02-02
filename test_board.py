import unittest
from board import init_board

class TestBoardInit(unittest.TestCase):

    def setUp(self):
        self.board = init_board()

    def test_board_initialization(self):

        expectation = [
                ['*"', '*"', '*"', '*"', '*"', '*"', '*"', '*"'],
                ['*"', '*"', '*"', '*"', '*"', '*"', '*"', '*"'],
                ['*"', '*"', '*"', '*"', '*"', '*"', '*"', '*"'],
                ['*"', '*"', '*"', '*"', '*"', '*"', '*"', '*"'],
                ['*"', '*"', '*"', '*"', '*"', '*"', '*"', '*"'],
                ['*"', '*"', '*"', '*"', '*"', '*"', '*"', '*"'],
                ['*"', '*"', '*"', '*"', '*"', '*"', '*"', '*"'],
                ['*"', '*"', '*"', '*"', '*"', '*"', '*"', '*"'],
            ]
    
        self.assertEqual(expectation, self.board)



if __name__ == '__main__':
    unittest.main()
