import unittest
from puzzle import Puzzle
from heuristics import heuristic_manhattan, heuristic_misplaced_tiles, heuristic_euclidean

class TestPuzzle(unittest.TestCase):
    def test_initial_state(self):
        puzzle = Puzzle([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
        self.assertEqual(puzzle.state, [[1, 2, 3], [4, 5, 6], [7, 8, 0]])

    def test_move(self):
        # Caso inicial
        puzzle = Puzzle([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
        
        # Movimiento hacia arriba
        puzzle.move('up')
        self.assertEqual(puzzle.state, [[1, 2, 3], [4, 5, 0], [7, 8, 6]])
        
        # Movimiento hacia abajo (deshacer el movimiento anterior)
        puzzle.move('down')
        self.assertEqual(puzzle.state, [[1, 2, 3], [4, 5, 6], [7, 8, 0]])
        
        # Movimiento hacia la izquierda
        puzzle.move('left')
        self.assertEqual(puzzle.state, [[1, 2, 3], [4, 5, 6], [7, 0, 8]])
        
        # Movimiento hacia la derecha (deshacer el movimiento anterior)
        puzzle.move('right')
        self.assertEqual(puzzle.state, [[1, 2, 3], [4, 5, 6], [7, 8, 0]])

        # Movimiento en diferentes posiciones
        puzzle = Puzzle([[1, 2, 3], [4, 0, 5], [7, 8, 6]])
        puzzle.move('up')
        self.assertEqual(puzzle.state, [[1, 0, 3], [4, 2, 5], [7, 8, 6]])
        
        puzzle.move('down')
        self.assertEqual(puzzle.state, [[1, 2, 3], [4, 0, 5], [7, 8, 6]])

    def test_heuristics(self):
        # Estado objetivo
        goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        
        # Estado igual al objetivo
        state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        self.assertEqual(heuristic_manhattan(state, goal), 0)
        self.assertEqual(heuristic_misplaced_tiles(state, goal), 0)
        self.assertEqual(heuristic_euclidean(state, goal), 0)

        # Estado no objetivo
        state = [[1, 2, 3], [4, 0, 5], [7, 8, 6]]
        self.assertEqual(heuristic_manhattan(state, goal), 2)
        self.assertEqual(heuristic_misplaced_tiles(state, goal), 2)
        self.assertEqual(heuristic_euclidean(state, goal), 2)

if __name__ == '__main__':
    unittest.main()