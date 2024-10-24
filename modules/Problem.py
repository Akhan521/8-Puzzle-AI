# Importing heapq to use as our min heap.
import heapq
# Importing our State class from State.py.
from modules.State import State

class Problem:
    def __init__(self, initial_state, goal_state):
        self.rows = 3
        self.cols = 3
        # To store our states in the order we visit them.
        self.states = [initial_state]
        self.frontier = []
        # Our initial state.
        self.initial_state = initial_state
        # Our goal state.
        self.goal_state = goal_state
        # The correct position of each tile.
        self.tile_map = {
            1: (0,0),
            2: (0,1),
            3: (0,2),
            4: (1,0),
            5: (1,1),
            6: (1,2),
            7: (2,0),
            8: (2,1),
        }

    # Get all states thus far.
    def get_states(self):
        return self.states
    # Print the current state.
    def print_current_state(self):
        self.states[-1].print_state()
    # Get the total cost of the current state.
    def get_total_cost_mt(self):
        return self.states[-1].get_total_cost_mt(self.goal_state, self.tile_map)
    # Get the position of the empty tile.
    def get_empty_tile_pos(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.states[-1].state[i][j] == 0:
                    return i, j
    # Find the positions that can be moved into the empty tile.
    def get_possible_moves(self):
        empty_tile_pos = self.get_empty_tile_pos()
        possible_moves = []
        all_directions = [(0,1), (0,-1), (1,0), (-1,0)]

        for direction_offset in all_directions:
            x_offset, y_offset = direction_offset
            new_x = empty_tile_pos[0] + x_offset
            new_y = empty_tile_pos[1] + y_offset
            if new_x >= 0 and new_x < self.rows and new_y >= 0 and new_y < self.cols:
                possible_moves.append((new_x, new_y))

        return possible_moves
    # Making a move into the empty tile.
    def make_move(self):
        possible_moves = self.get_possible_moves()
        empty_tile_pos = self.get_empty_tile_pos()
        empty_i, empty_j = empty_tile_pos
        new_states = []
        # Let's consider all the moves we can make.
        for move in possible_moves:
            i,j = move
            # We need a copy of the current state.
            current_state_copy = [row[:] for row in self.states[-1].state]
            new_state = State(current_state_copy)
            new_state.state[empty_i][empty_j], new_state.state[i][j] = new_state.state[i][j], new_state.state[empty_i][empty_j]
            new_state_cost = new_state.get_total_cost_mt(self.goal_state, self.tile_map)
            new_states.append((new_state_cost, new_state))
        for state in new_states:
            self.frontier.append(state)
        heapq.heapify(self.frontier)
        for state in self.frontier:
            print("cost: ", state[0])
            state[1].print_state()
        
    
    
    