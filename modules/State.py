# A class representing a state in our 8 puzzle game.

class State:
    def __init__(self, state, rows=3, cols=3):
        # The dimensions of our puzzle.
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

    # Computes the total cost of a function using the Misplaced tile heuristic.
    def compute_total_cost_mt(self, num_moves, goal_state, tile_map):
        self.compute_cost(num_moves)
        self.compute_heuristic_mt(goal_state, tile_map)
        self.fn = self.gn + self.hn
    # Retrieves the total cost using the MT heuristic.
    def get_total_cost_mt(self, num_moves, goal_state, tile_map):
        self.compute_total_cost_mt(num_moves, goal_state, tile_map)
        return self.fn

    # Computes the total cost of a function using the Euclidean distance
    def compute_total_cost_euc(self, num_moves, goal_state, tile_map):
        self.compute_cost(num_moves)
        self.compute_heuristic_euc(goal_state, tile_map)
        self.fn = self.gn + self.hn

    #Retrieves (like a dog) the total cost using EUC heuristic
    def get_total_cost_euc(self, num_moves, goal_state, tile_map):
        self.compute_total_cost_euc(num_moves, goal_state, tile_map)
        return self.fn
    
    # Computes the cost of a state.
    def compute_cost(self, num_moves):
        # The cost of a state is the number of moves it took to get to that state.
        self.gn = num_moves
        return self.gn
    # Retrieves the cost of a state.
    def get_cost(self, num_moves):
        self.compute_cost(num_moves)
        return self.gn
    
    # Computes the heuristic value of a state using the Manhattan distance/Misplaced tile heuristic.
    def compute_heuristic_mt(self, goal_state, tile_map):
        h_val = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if self.state[i][j] != 0 and self.state[i][j] != goal_state[i][j]:
                    goal_i, goal_j = tile_map[self.state[i][j]]
                    h_val += abs(i - goal_i) + abs(j - goal_j)
        self.hn = h_val
    # Retrieves the heuristic value of a state (the MT heuristic).
    def get_heuristic_mt(self, goal_state, tile_map):
        self.compute_heuristic_mt(goal_state, tile_map)
        return self.hn

    # Compute the heuristic value of a state using the Euclidean distance
    def compute_heuristic_euc(self, goal_state, tile_map):
        h_val = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if self.state[i][j] != 0 and self.state[i][j] != goal_state[i][j]:
                    goal_i, goal_j = tile_map[self.state[i][j]]
                    h_val += (((i - goal_i)** 2) + ((j - goal_j)** 2)) ** .5
        self.hn = h_val

    def get_heuristic_euc(self, goal_state, tile_map):
        self.compute_heuristic_euc(goal_state, tile_map)
        return self.hn

    # Setters and getters for the state.
    def set_state(self, state):
        self.state = state
    def get_state(self):
        return self.state
    # Prints the state.
    def print_state(self):
        for row in self.state:
            print(row)
        print()