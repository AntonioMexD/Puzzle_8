import pandas as pd
import time
from puzzle import Puzzle
from search import a_star_search, greedy_search
from heuristics import heuristic_manhattan, heuristic_misplaced_tiles, heuristic_euclidean
from utils import generate_random_puzzle, is_solvable

# Parámetros de prueba
num_experiments = 1000

# Almacenar resultados
results = []

def run_experiment():
    for i in range(num_experiments):
        initial_state = generate_random_puzzle()
        if not is_solvable(initial_state):
            continue  # Saltar estados no solucionables

        puzzle = Puzzle(initial_state)
        for search_algorithm, name in [(a_star_search, 'A*'), (greedy_search, 'Greedy')]:
            for heuristic, heuristic_name in [
                (heuristic_manhattan, 'heuristic_manhattan'),
                (heuristic_misplaced_tiles, 'heuristic_misplaced_tiles'),
                (heuristic_euclidean, 'heuristic_euclidean')
            ]:
                start_time = time.time()
                result = search_algorithm(puzzle, heuristic)
                end_time = time.time()

                execution_time = end_time - start_time
                
                # Almacenar el resultado
                results.append({
                    'Initial State': initial_state,
                    'Search Algorithm': name,
                    'Heuristic': heuristic_name,
                    'Found Solution': result['found_solution'],
                    'Time': execution_time,
                    'Max Frontier Size': result['max_frontier_size']
                })

# Ejecutar experimentos
run_experiment()

# Crear un DataFrame y guardar en CSV
df = pd.DataFrame(results)
df.to_csv('experiments_results.csv', index=False)

print("Experimentos completos. Resultados guardados en 'experiments_results.csv'.")
