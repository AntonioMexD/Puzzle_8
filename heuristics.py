def heuristic_manhattan(state, goal):
    # Suma de las distancias Manhattan para cada ficha
    dist = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                x, y = divmod(goal.index(state[i][j]), 3)
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
    # Distancia Euclidiana para cada ficha
    dist = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                x, y = divmod(goal.index(state[i][j]), 3)
                dist += ((i - x)**2 + (j - y)**2)**0.5
    return dist
