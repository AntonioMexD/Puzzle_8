import random

def generate_random_puzzle():
    puzzle = list(range(9))
    random.shuffle(puzzle)
    return [puzzle[:3], puzzle[3:6], puzzle[6:]]

def is_solvable(puzzle):
    # Verifica si el estado es resoluble usando el número de inversiones
    flat_puzzle = [num for row in puzzle for num in row if num != 0]
    inversions = 0
    for i in range(len(flat_puzzle)):
        for j in range(i + 1, len(flat_puzzle)):
            if flat_puzzle[i] > flat_puzzle[j]:
                inversions += 1
    return inversions % 2 == 0
