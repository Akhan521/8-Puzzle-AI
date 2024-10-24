# Importing heapq to use as our min heap.
import heapq
# Importing our State class from State.py.
from modules.State import State

class Problem:
    # Our state id: a static variable used to keep track of the number of states we've considered.
    # It's also used as a secondary key in our heap to break ties when popping states.
    id = -1

    # Our constructor which initializes our problem.
    def __init__(self, initial_state, goal_state):
        # The dimensions of the 8 puzzle.
        self.rows = 3
        self.cols = 3
        # Our initial state.
        self.initial_state = initial_state
        # Our current state.
        self.current_state = initial_state
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
        # A set of the states we've seen.
        self.was_seen = set()

        # Defining our initial setup: the initial cost, the state id, and the state.
        initial_cost = self.initial_state.get_total_cost_mt(self.goal_state, self.tile_map)
        # Every triplet in the heap is of the form (cost, id, state).
        initial_setup = [(initial_cost, self.id, self.initial_state)]
        heapq.heapify(initial_setup)
        # Our frontier is implemented as a min heap.
        self.frontier = initial_setup

    # Get the current state.
    def get_state(self):
        return self.current_state
    
    # Print the current state.
    def print_current_state(self):
        self.current_state.print_state()

    # Get the total cost of the current state.
    def get_total_cost_mt(self):
        return self.current_state.get_total_cost_mt(self.goal_state, self.tile_map)
    
    # Get the position of the empty tile.
    def get_empty_tile_pos(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.current_state.state[i][j] == 0:
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
    
    # Making a move into the empty tile using the MT heuristic.
    def make_move_using_mt(self):
        popped_state = None
        # As long as we have states to consider...
        while len(self.frontier) > 0:
            # We pop the state w/ the min cost. Recall that our triplets are of the form (cost, id, state).
            popped_state = heapq.heappop(self.frontier)[2]
            # If we haven't seen this state before, we can process it.
            if str(popped_state.state) not in self.was_seen:
                # Mark the state as seen as we'll be processing it now.
                self.was_seen.add(str(popped_state.state))
                break
            # Otherwise, we need to keep popping states until we find one we haven't seen before.
            else:
                popped_state = None
        # If no new states were found, we have reached a dead end.
        if popped_state == None:
            print("There are no more possible moves.")
            return
        
        # Now, we can begin to process the popped state.
        self.current_state = popped_state
        # Get all the possible moves we can make from the current state.
        possible_moves = self.get_possible_moves()
        # Get the position of the empty tile.
        empty_tile_pos = self.get_empty_tile_pos()
        empty_i, empty_j = empty_tile_pos
        # A list to store the new states we can reach from the current state.
        new_states = []

        # Let's consider all the moves we can make.
        for move in possible_moves:
            i,j = move
            # We need a copy of the current state.
            current_state_copy = [row[:] for row in self.current_state.state]
            new_state = State(current_state_copy)
            # Swap the empty tile with the tile we want to move.
            new_state.state[empty_i][empty_j], new_state.state[i][j] = new_state.state[i][j], new_state.state[empty_i][empty_j]
            new_state_cost = new_state.get_total_cost_mt(self.goal_state, self.tile_map)
            # As we've produced a new state, we need to increment our state id.
            self.id += 1
            # We can then add the new state to our list of new states.
            new_states.append((new_state_cost, self.id, new_state))
        
        # Next, we need to add the states we haven't seen to our frontier.
        # Recall that our triplets are of the form (cost, id, state).
        for state_triplet in new_states:
            # We store our state (a State object).
            state = state_triplet[2] 
            # If we haven't seen this state before, we can add it to our frontier.
            if str(state.state) not in self.was_seen:
                # We add the state triplet to our frontier.
                heapq.heappush(self.frontier, state_triplet)
        
    # Solve the prolem using the MT heuristic.
    def solve_using_mt(self):
        # As long as we haven't reached the goal state...
        while self.current_state.state != self.goal_state:
            # We make a move using the MT heuristic.
            self.make_move_using_mt()
            #print("Total Cost: ", self.get_total_cost_mt())

        # Once we've reached the goal state, we claim our VICTORY!
        print("You have solved the puzzle!")
        print("Final State: ")
        self.print_current_state()
    
    