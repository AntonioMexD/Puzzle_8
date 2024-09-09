# Puzzle 8

## Descripción

Puzzle 8 es un juego de rompecabezas clásico en el que debes ordenar las piezas deslizables en una matriz 3x3 para alcanzar el estado objetivo. Este proyecto implementa y compara dos algoritmos de búsqueda (`A*` y `Greedy`) utilizando tres heurísticas (`Manhattan`, `Fichas Mal Colocadas`, y `Euclidiana`).

## Estructura del Proyecto

- `game.py`: Lógica del juego y manejo de la interfaz.
- `puzzle.py`: Definición de la clase `Puzzle`, que maneja el estado y las operaciones del rompecabezas.
- `search.py`: Implementación de los algoritmos de búsqueda (`a_star_search` y `greedy_search`).
- `heuristics.py`: Definición de las heurísticas utilizadas en la búsqueda.
- `utils.py`: Funciones auxiliares como la generación de rompecabezas aleatorios y la verificación de si un rompecabezas es solucionable.
- `main.py`: Punto de entrada para ejecutar el juego y los experimentos.
- `view_results.py`: Visualización de los resultados experimentales.
- `experiments.py`: Código para ejecutar los experimentos y almacenar los resultados.
- `experiments_results.csv`: Archivo CSV con los resultados experimentales.
- `Tests/test_heuristic.py`, `test_puzzle.py`, `test_utils.py`: Pruebas unitarias para los diferentes módulos del proyecto.

## Requisitos

- Python 3.x
- Pygame

Puedes instalar las dependencias necesarias ejecutando:

```bash
pip install pygame pandas

Uso

Ejecutar el Juego
Para iniciar el juego, ejecuta:

bash
Copiar código
python main.py
Ejecutar Experimentos
Para ejecutar los experimentos y generar los resultados, ejecuta:

bash
Copiar código
python experiments.py
Los resultados se guardarán en experiments_results.csv.

Pruebas Unitarias
Para ejecutar las pruebas unitarias, puedes usar pytest:

bash
Copiar código
pytest
Controles

Flechas Izquierda/Derecha/Arriba/Abajo: Mover las fichas en la dirección deseada.
Resultados Experimentales

El archivo experiments_results.csv contiene los resultados de 1000 experimentos, incluyendo el estado inicial, el algoritmo de búsqueda utilizado, la heurística, si se encontró una solución, el tiempo de ejecución y el tamaño máximo de la frontera.

Contribuciones

Si deseas contribuir al proyecto, por favor haz un fork del repositorio y envía tus pull requests. Asegúrate de que tu código pase todas las pruebas y esté bien documentado.
