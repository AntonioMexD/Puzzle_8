import unittest
from utils import generate_random_puzzle, is_solvable

class TestUtils(unittest.TestCase):

    def test_generate_random_puzzle():
        puzzle = generate_random_puzzle()
        assert len(puzzle) == 3
        assert len(puzzle[0]) == 3
        assert len(set(map(tuple, puzzle))) == 9  # Debe haber 9 fichas únicas
        assert sorted([num for row in puzzle for num in row]) == list(range(9))  # Debe contener números del 0 al 8

    def test_is_solvable():
        solvable_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        unsolvable_state = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]
        assert is_solvable(solvable_state) is True
        assert is_solvable(unsolvable_state) is False

if __name__ == '__main__':
    unittest.main()