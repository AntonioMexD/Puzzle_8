from queue import PriorityQueue

# A* Search Algorithm
def a_star_search(puzzle, heuristic):
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    frontier = PriorityQueue()
    frontier.put((0, puzzle, 0))  # (costo total, puzzle, costo acumulado)
    explored = set()
    
    while not frontier.empty():
        _, current_puzzle, cost_so_far = frontier.get()

        if current_puzzle.is_goal(goal_state):
            return reconstruct_path(current_puzzle)  # Implementa esta función para reconstruir el camino
    

        explored.add(tuple(tuple(row) for row in current_puzzle.state))

        for neighbor in current_puzzle.get_successors():
            state_tuple = tuple(tuple(row) for row in neighbor.state)
            if state_tuple not in explored:
                cost = cost_so_far + 1  # Incrementa el costo acumulado
                heuristic_cost = heuristic(neighbor.state, goal_state)
                total_cost = cost + heuristic_cost
                frontier.put((total_cost, neighbor, cost))
    
    return None  # No se encontró solución

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


def reconstruct_path(end_puzzle):
    # Implementa la lógica para reconstruir el camino desde el rompecabezas final hasta el inicial
    path = []
    current = end_puzzle
    while current:
        path.append(current)
        current = current.parent  # Si has mantenido una referencia al padre en el rompecabezas
    path.reverse()
    return path