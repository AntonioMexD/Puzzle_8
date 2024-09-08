def heuristic_manhattan(state, goal):
    # Aplana la lista de estado objetivo para búsquedas más fáciles
    flat_goal = [tile for row in goal for tile in row]
    dist = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            tile = state[i][j]
            if tile != 0:
                # Encuentra la posición de la ficha en el estado objetivo
                index = flat_goal.index(tile)
                x, y = divmod(index, len(goal))
                dist += abs(i - x) + abs(j - y)
    return dist


def heuristic_misplaced_tiles(state, goal):
    # Contar las fichas mal colocadas
    misplaced = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                misplaced += 1
    return misplaced

def heuristic_euclidean(state, goal):
    flat_goal = [tile for row in goal for tile in row]
    dist = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            tile = state[i][j]
            if tile != 0:
                index = flat_goal.index(tile)
                x, y = divmod(index, len(goal))
                dist += ((i - x) ** 2 + (j - y) ** 2) ** 0.5
    return dist

