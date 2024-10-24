# A class representing a state in our 8 puzzle game.

class State:
    def __init__(self, state, rows=3, cols=3):
        self.rows = rows
        self.cols = cols
        # Our state represented as a 2D array.
        self.state = state
        # The cost of our state.
        self.gn = 0
        # The heuristic value of our state.
        self.hn = 0
        # The total cost of our state.
        self.fn = 0

    # Setters and getters for the total cost.
    def compute_total_cost_mt(self, goal_state, tile_map):
        self.compute_cost(goal_state)
        self.compute_heuristic_mt(goal_state, tile_map)
        self.fn = self.gn + self.hn
    def get_total_cost_mt(self, goal_state, tile_map):
        self.compute_total_cost_mt(goal_state, tile_map)
        return self.fn
    
    # Setters and getters for the cost g(n).
    def compute_cost(self, goal_state):
        cost = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if self.state[i][j] != goal_state[i][j]:
                    cost += 1
        self.gn = cost

    def get_cost(self, goal_state):
        self.compute_cost(goal_state)
        return self.gn
    
    # Setters and getters for the heuristic h(n).
    def compute_heuristic_mt(self, goal_state, tile_map): # Manhattan distance/Misplaced tile heuristic.
        h_val = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if self.state[i][j] != 0 and self.state[i][j] != goal_state[i][j]:
                    goal_i, goal_j = tile_map[self.state[i][j]]
                    h_val += abs(i - goal_i) + abs(j - goal_j)
        self.hn = h_val
            
    def get_heuristic_mt(self, goal_state):
        self.compute_heuristic_mt(goal_state)
        return self.hn
    
    # Setters and getters for the state.
    def set_state(self, state):
        self.state = state
    def get_state(self):
        return self.state
    
    def print_state(self):
        for row in self.state:
            print(row)
        print()