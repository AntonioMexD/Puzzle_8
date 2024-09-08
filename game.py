import pygame
from puzzle import Puzzle
from search import a_star_search
from heuristics import heuristic_manhattan

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

def main():
    running = True
    puzzle = Puzzle([[1, 2, 3], [4, 5, 6], [7, 8, 0]])  # Estado inicial resuelto

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
                    solution = a_star_search(puzzle, heuristic_manhattan)
                    if solution:
                        print("Solución encontrada")
                        for step in solution:
                            step.display()
        
        # Dibujar el tablero
        draw_puzzle(puzzle)

    pygame.quit()

if __name__ == "__main__":
    main()
