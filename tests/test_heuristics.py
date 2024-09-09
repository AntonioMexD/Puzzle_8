import unittest
from heuristics import heuristic_manhattan, heuristic_misplaced_tiles, heuristic_euclidean

class TestHeuristics(unittest.TestCase):

    def test_heuristic_manhattan():
        # Caso base: estado y objetivo iguales
        state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        assert heuristic_manhattan(state, goal) == 0

        # Caso con fichas desplazadas
        state = [[1, 2, 0], [4, 5, 3], [7, 8, 6]]
        goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        assert heuristic_manhattan(state, goal) == 4  # Calcula la distancia de las fichas 3 y 6

        # Caso con una ficha fuera de lugar
        state = [[1, 2, 3], [4, 6, 5], [7, 8, 0]]
        goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        assert heuristic_manhattan(state, goal) == 2  # Calcula la distancia de la ficha 6

    def test_heuristic_misplaced_tiles():
        # Caso base: estado y objetivo iguales
        state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        assert heuristic_misplaced_tiles(state, goal) == 0

        # Caso con fichas desplazadas
        state = [[1, 2, 0], [4, 5, 3], [7, 8, 6]]
        goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        assert heuristic_misplaced_tiles(state, goal) == 3  # Fichas mal colocadas: 3, 6, 0

        # Caso con una ficha fuera de lugar
        state = [[1, 2, 3], [4, 6, 5], [7, 8, 0]]
        goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        assert heuristic_misplaced_tiles(state, goal) == 1  # Ficha mal colocada: 6

    def test_heuristic_euclidean():
        # Caso base: estado y objetivo iguales
        state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        assert heuristic_euclidean(state, goal) == 0

        # Caso con fichas desplazadas
        state = [[1, 2, 0], [4, 5, 3], [7, 8, 6]]
        goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        assert round(heuristic_euclidean(state, goal), 4) == 5.6569  # Calcula la distancia euclidiana de las fichas 3 y 6

        # Caso con una ficha fuera de lugar
        state = [[1, 2, 3], [4, 6, 5], [7, 8, 0]]
        goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        assert round(heuristic_euclidean(state, goal), 4) == 2.8284  # Calcula la distancia euclidiana de la ficha 6

if __name__ == '__main__':
    unittest.main()