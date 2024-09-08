
class Puzzle:
    def __init__(self, initial_state, cost=0, parent=None):
        self.state = initial_state
        self.size = 3
        self.cost = cost
        self.parent = parent

    def __lt__(self, other):
        return self.cost < other.cost

    def get_empty_tile_position(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.state[i][j] == 0:
                    return (i, j)

    def move(self, direction):
        i, j = self.get_empty_tile_position()
        if direction == 'up' and i > 0:
            self.state[i][j], self.state[i-1][j] = self.state[i-1][j], self.state[i][j]
        elif direction == 'down' and i < self.size - 1:
            self.state[i][j], self.state[i+1][j] = self.state[i+1][j], self.state[i][j]
        elif direction == 'left' and j > 0:
            self.state[i][j], self.state[i][j-1] = self.state[i][j-1], self.state[i][j]
        elif direction == 'right' and j < self.size - 1:
            self.state[i][j], self.state[i][j+1] = self.state[i][j+1], self.state[i][j]
    
    def is_goal(self, goal_state):
        return self.state == goal_state
    
    def display(self):
        for row in self.state:
            print(row)
        print()

    def get_successors(self):
        successors = []
        for direction in ['up', 'down', 'left', 'right']:
            new_puzzle = Puzzle([row[:] for row in self.state], parent=self)
            new_puzzle.move(direction)
            successors.append(new_puzzle)
        return successors
