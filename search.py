from queue import PriorityQueue

def a_star_search(puzzle, heuristic):
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    frontier = PriorityQueue()
    frontier.put((0, puzzle))
    explored = set()
    
    while not frontier.empty():
        _, current_puzzle = frontier.get()

        if current_puzzle.is_goal(goal_state):
            return [current_puzzle]  # La solución es solo el estado final por simplicidad

        explored.add(tuple(tuple(row) for row in current_puzzle.state))

        for neighbor in current_puzzle.get_successors():
            if tuple(tuple(row) for row in neighbor.state) not in explored:
                cost = heuristic(neighbor.state, goal_state)
                frontier.put((cost, neighbor))
    
    return None  # No se encontró solución

def greedy_search(puzzle, heuristic):
    # Similar al A*, pero solo usando la heurística sin considerar el costo total
    pass
