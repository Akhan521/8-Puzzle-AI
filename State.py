# A class representing a state in our 8 puzzle game.

class State:
    def __init__(self, state):
        # Our state represented as a 2D array.
        self.state = state
        # The cost of our state.
        self.gn = 0
        # The heuristic value of our state.
        self.hn = 0
        # The total cost of our state.
        self.fn = 0

    # Setters and getters for the total cost.
    def set_total_cost(self):
        self.fn = self.gn + self.hn
    def get_total_cost(self):
        return self.fn
    
    # Setters and getters for the cost g(n).
    def set_cost(self, cost):
        self.gn = cost
    def get_cost(self):
        return self.gn
    
    # Setters and getters for the heuristic h(n).
    def set_heuristic(self, heuristic):
        self.hn = heuristic
    def get_heuristic(self):
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