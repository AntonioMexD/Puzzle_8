import random

def generate_random_puzzle():
    puzzle = list(range(9))
    random.shuffle(puzzle)
    return [puzzle[i:i+3] for i in range(0, 9, 3)]  # Garantiza una estructura de 3x3


def is_solvable(puzzle):
    # Verifica si el estado es resoluble usando el número de inversiones
    flat_puzzle = [num for row in puzzle for num in row if num != 0]
    inversions = 0
    for i in range(len(flat_puzzle)):
        for j in range(i + 1, len(flat_puzzle)):
            if flat_puzzle[i] > flat_puzzle[j]:
                inversions += 1
    return inversions % 2 == 0
