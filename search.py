from queue import PriorityQueue
import time

# A* Search Algorithm
def a_star_search(puzzle, heuristic):
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    frontier = PriorityQueue()
    frontier.put((0, puzzle, 0))  # (costo total, puzzle, costo acumulado)
    explored = set()
    
    start_time = time.time()
    max_frontier_size = 0
    
    while not frontier.empty():
        _, current_puzzle, cost_so_far = frontier.get()
        
        max_frontier_size = max(max_frontier_size, frontier.qsize())

        if current_puzzle.is_goal(goal_state):
            elapsed_time = time.time() - start_time  # Tiempo final
            path, moves = reconstruct_path(current_puzzle)  # Camino y movimientos de solución
            return {
                'solution': path,  # Camino solución
                'moves': moves,    # Movimientos realizados
                'time': elapsed_time,  # Tiempo total
                'max_frontier_size': max_frontier_size,  # Tamaño máximo de la frontera
                'found_solution': True  # Solución encontrada
            }

        explored.add(tuple(tuple(row) for row in current_puzzle.state))

        for neighbor in current_puzzle.get_successors():
            state_tuple = tuple(tuple(row) for row in neighbor.state)
            if state_tuple not in explored:
                cost = cost_so_far + 1  # Incrementa el costo acumulado
                heuristic_cost = heuristic(neighbor.state, goal_state)
                total_cost = cost + heuristic_cost
                neighbor.parent = current_puzzle
                neighbor.move = get_move_direction(current_puzzle, neighbor)  # Obtener el movimiento realizado
                frontier.put((total_cost, neighbor, cost))
    
    elapsed_time = time.time() - start_time  # Tiempo final
    return {
        'solution': None,  # No hay solución
        'moves': None,     # No hay movimientos
        'time': elapsed_time,  # Tiempo total
        'max_frontier_size': max_frontier_size,  # Tamaño máximo de la frontera
        'found_solution': False  # Solución no encontrada
    }

def get_move_direction(previous_puzzle, current_puzzle):
    """Determina el movimiento realizado entre dos estados del rompecabezas."""
    prev_state = previous_puzzle.state
    curr_state = current_puzzle.state
    for i in range(len(prev_state)):
        for j in range(len(prev_state[i])):
            if prev_state[i][j] != curr_state[i][j]:
                return determine_move(prev_state, curr_state, i, j)
    return None

def determine_move(prev_state, curr_state, i, j):
    """Determina la dirección del movimiento (arriba, abajo, izquierda, derecha)."""
    zero_pos_prev = find_zero(prev_state)
    zero_pos_curr = find_zero(curr_state)
    if zero_pos_prev[0] == zero_pos_curr[0]:
        return 'left' if zero_pos_prev[1] > zero_pos_curr[1] else 'right'
    else:
        return 'up' if zero_pos_prev[0] > zero_pos_curr[0] else 'down'

def find_zero(state):
    """Encuentra la posición del 0 en el estado del rompecabezas."""
    for i, row in enumerate(state):
        for j, value in enumerate(row):
            if value == 0:
                return (i, j)
    return None

def reconstruct_path(end_puzzle):
    path = []
    moves = []
    current = end_puzzle
    while current:
        path.append(current)
        if current.move:  # Si el movimiento actual no es nulo
            moves.append(current.move)  # Guardar el movimiento realizado como una cadena
        current = current.parent  # Si has mantenido una referencia al padre en el rompecabezas
    path.reverse()
    moves.reverse()  # Invertir los movimientos para que estén en el orden correcto
    return path, moves

def greedy_search(puzzle, heuristic):
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    frontier = PriorityQueue()
    frontier.put((0, puzzle))  # Solo el costo heurístico
    explored = set()
    
    while not frontier.empty():
        _, current_puzzle = frontier.get()

        if current_puzzle.is_goal(goal_state):
            return [current_puzzle]  # La solución es solo el estado final por simplicidad

        explored.add(tuple(tuple(row) for row in current_puzzle.state))

        for neighbor in current_puzzle.get_successors():
            state_tuple = tuple(tuple(row) for row in neighbor.state)
            if state_tuple not in explored:
                heuristic_cost = heuristic(neighbor.state, goal_state)
                frontier.put((heuristic_cost, neighbor))
    
    return None  # No se encontró solución
