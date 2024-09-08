import pygame
from puzzle import Puzzle
from search import a_star_search
from heuristics import heuristic_manhattan
from utils import generate_random_puzzle, is_solvable

# Inicializar Pygame
pygame.init()

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Dimensiones de la pantalla
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300
TILE_SIZE = 100

# Crear la ventana
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('8-Puzzle')

# Fuente para el texto
font = pygame.font.Font(None, 74)

def draw_puzzle(puzzle):
    screen.fill(WHITE)
    for i in range(puzzle.size):
        for j in range(puzzle.size):
            tile = puzzle.state[i][j]
            if tile != 0:  # No dibujar el espacio vacío
                pygame.draw.rect(screen, BLUE, (j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                text = font.render(str(tile), True, WHITE)
                screen.blit(text, (j * TILE_SIZE + 30, i * TILE_SIZE + 20))
    pygame.display.flip()

def run_game():
    running = True
    puzzle = None

    # Generar un rompecabezas válido
    while puzzle is None:
        initial_state = generate_random_puzzle()
        if is_solvable(initial_state):
            puzzle = Puzzle(initial_state)
    
    print("Estado inicial del rompecabezas:", puzzle.state)  # Depuración

    solution_steps = []  # Pasos de la solución
    moves = []  # Movimientos realizados

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    puzzle.move('up')
                elif event.key == pygame.K_DOWN:
                    puzzle.move('down')
                elif event.key == pygame.K_LEFT:
                    puzzle.move('left')
                elif event.key == pygame.K_RIGHT:
                    puzzle.move('right')
                
                # Resolver automáticamente usando A* con la heurística de Manhattan
                elif event.key == pygame.K_SPACE:
                    result = a_star_search(puzzle, heuristic_manhattan)
                    
                    if result['found_solution']:
                        print("Solución encontrada")
                        print(f"Tiempo de resolución: {result['time']:.4f} segundos")
                        print(f"Tamaño máximo de la frontera: {result['max_frontier_size']}")
                        solution_steps = result['solution']
                        moves = result['moves']  # Obtener los movimientos
                        print("Movimientos realizados:", moves)  # Imprimir los movimientos
                    else:
                        print("No se encontró solución")
                        print(f"Tiempo de ejecución: {result['time']:.4f} segundos")
                        print(f"Tamaño máximo de la frontera: {result['max_frontier_size']}")
                            

        # Dibujar el tablero
        draw_puzzle(puzzle)
                
        if solution_steps:
            for step in solution_steps:
                screen.fill(WHITE)  # Limpiar la pantalla
                draw_puzzle(step)   # Dibujar el estado actual del rompecabezas
                pygame.display.flip()  # Actualizar la pantalla
                pygame.time.delay(500)  # Pausa para ver la transición entre pasos
                puzzle = step  # Actualizar el estado del rompecabezas

    pygame.quit()

