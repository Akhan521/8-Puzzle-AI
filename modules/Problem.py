# Importing heapq to use as our min heap.
import heapq
# Importing our State class from State.py.
from modules.State import State

class Problem:
    # Our state id: a static variable used to keep track of the number of states we've considered.
    # It's also used as a secondary key in our heap to break ties when popping states.
    id = 0
    # Number of nodes we've expanded.
    nodes_expanded = 0
    # To store the max number of nodes in our frontier at any given time.
    max_nodes = 0

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
        # The number of moves we've made.
        self.moves = 0
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

    # Get the current state.
    def get_state(self):
        return self.current_state
    
    # Get the number of moves made.
    def get_moves(self):
        return self.moves
    
    # Print the current state.
    def print_current_state(self):
        self.current_state.print_state()

    # Get the total cost of the current state. (Manhattan Distance)
    def get_total_cost_md(self):
        return self.current_state.get_total_cost_md(self.moves, self.goal_state, self.tile_map)
    
    # Get the total cost of the current state. (Misplaced Tiles)
    def get_total_cost_mt(self):
        return self.current_state.get_total_cost_mt(self.moves, self.goal_state)

    # Get the total cost of the current state. (Euclidean)
    def get_total_cost_euc(self):
        return self.current_state.get_total_cost_euc(self.moves, self.goal_state, self.tile_map)

    # Get the cost of the current state.
    def get_cost(self):
        return self.current_state.get_cost(self.moves)
    
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
    
    # Making a move into the empty tile using Uniform Cost Search (Only the cost is considered, not the heuristic).
    def make_move_using_ucs(self):
        popped_state = None
        # As long as we have states to consider...
        while len(self.frontier) > 0:
            # We pop the state w/ the min cost. Recall that our quadruples are of the form (cost, id, state, moves).
            popped_state_quadruple = heapq.heappop(self.frontier)
            popped_state = popped_state_quadruple[2]
            # If we haven't seen this state before, we can process it.
            if str(popped_state.state) not in self.was_seen:
                # Mark the state as seen as we'll be processing it now.
                self.was_seen.add(str(popped_state.state))
                break # Breaking out once we have a state to process.
            # Otherwise, we need to keep popping states until we find one we haven't seen before.
            else:
                popped_state = None
        # If no new states were found, we have reached a dead end.
        if popped_state == None:
            print("There are no more possible moves.")
            self.moves = -1 # Setting the number of moves to -1 to indicate that the puzzle is unsolvable.
            return
        
        # If we've reached our goal state, we save some info and return.
        if popped_state.state == self.goal_state:
            self.current_state = popped_state
            self.moves = popped_state_quadruple[3]
            gn = popped_state.get_cost(popped_state_quadruple[3])
            print(f"The final state w/ g(n)={gn} is...")
            popped_state.print_state()
            return
        
        # The diameter of the puzzle is 31, so we can't have more than 31 moves.
        if popped_state_quadruple[3] > 31:
            print("The puzzle is unsolvable.")
            self.moves = -1 # Setting the number of moves to -1 to indicate that the puzzle is unsolvable.
            return
        
        # Some helpful text to let us know we're making progress.
        gn = popped_state.get_cost(popped_state_quadruple[3])
        print(f"The best state to expand w/ g(n)={gn} is...")
        popped_state.print_state()
        print()
        # Increment the number of nodes we've expanded.
        self.nodes_expanded += 1
        # Now, we can begin to process the popped state.
        self.current_state = popped_state
        # Storing the number of moves we've made to reach our current state.
        num_moves = popped_state_quadruple[3]
        self.moves = num_moves
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
            # Storing the number of moves we've made to reach our current state.
            num_moves = popped_state_quadruple[3]
            # We need a copy of the current state.
            current_state_copy = [row[:] for row in self.current_state.state]
            new_state = State(current_state_copy)
            # Swap the empty tile with the tile we want to move.
            new_state.state[empty_i][empty_j], new_state.state[i][j] = new_state.state[i][j], new_state.state[empty_i][empty_j]
            # For Uniform Cost Search, we only consider the cost of the state (i.e. the moves to reach the current state).
            num_moves += 1
            new_state_cost = num_moves
            # As we've produced a new state, we need to increment our state id.
            self.id += 1
            # We can then add the new state to our list of new states.
            new_states.append((new_state_cost, self.id, new_state, num_moves))
        
        # Next, we need to add the states we haven't seen to our frontier.
        # Recall that our quadruples are of the form (cost, id, state, moves).
        for state_quadruple in new_states:
            # We store our state (a State object).
            state = state_quadruple[2] 
            # If we haven't seen this state before, we can add it to our frontier.
            if str(state.state) not in self.was_seen:
                # We add the state triplet to our frontier.
                heapq.heappush(self.frontier, state_quadruple)
                self.max_nodes = max(self.max_nodes, len(self.frontier))
    
    # Making a move into the empty tile using the MD heuristic.
    def make_move_using_md(self):
        popped_state = None
        # As long as we have states to consider...
        while len(self.frontier) > 0:
            # We pop the state w/ the min cost. Recall that our quadruples are of the form (cost, id, state, moves).
            popped_state_quadruple = heapq.heappop(self.frontier)
            popped_state = popped_state_quadruple[2]
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
            self.moves = -1 # Setting the number of moves to -1 to indicate that the puzzle is unsolvable.
            return
        
        # If we've reached our goal state, we save some info and return.
        if popped_state.state == self.goal_state:
            self.current_state = popped_state
            self.moves = popped_state_quadruple[3]
            gn = popped_state.get_cost(popped_state_quadruple[3])
            hn = popped_state.get_heuristic_md(self.goal_state, self.tile_map)
            print(f"The final state w/ g(n)={gn} and h(n)={hn} is...")
            popped_state.print_state()
            return
        
        # The diameter of the puzzle is 31, so we can't have more than 31 moves.
        if popped_state_quadruple[3] > 31:
            print("The puzzle is unsolvable.")
            self.moves = -1 # Setting the number of moves to -1 to indicate that the puzzle is unsolvable.
            return
        
        # Some helpful text to let us know we're making progress.
        gn = popped_state.get_cost(popped_state_quadruple[3])
        hn = popped_state.get_heuristic_md(self.goal_state, self.tile_map)
        print(f"The best state to expand w/ g(n)={gn} and h(n)={hn} is...")
        popped_state.print_state()
        print()
        # Increment the number of nodes we've expanded.
        self.nodes_expanded += 1
        # Now, we can begin to process the popped state.
        self.current_state = popped_state
        # Storing the number of moves we've made to reach our current state.
        num_moves = popped_state_quadruple[3]
        self.moves = num_moves
        #print('Moves so far: ', self.moves)
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
            # Storing the number of moves we've made to reach our current state.
            num_moves = popped_state_quadruple[3]
            # We need a copy of the current state.
            current_state_copy = [row[:] for row in self.current_state.state]
            new_state = State(current_state_copy)
            # Swap the empty tile with the tile we want to move.
            new_state.state[empty_i][empty_j], new_state.state[i][j] = new_state.state[i][j], new_state.state[empty_i][empty_j]
            # For A* search w/ the MD heuristic, we consider the total cost of the state.
            num_moves += 1
            new_state_cost = new_state.get_total_cost_md(num_moves, self.goal_state, self.tile_map)
            # As we've produced a new state, we need to increment our state id.
            self.id += 1
            # We can then add the new state to our list of new states.
            new_states.append((new_state_cost, self.id, new_state, num_moves))
        
        # Next, we need to add the states we haven't seen to our frontier.
        # Recall that our quadruples are of the form (cost, id, state, moves).
        for state_quadruple in new_states:
            # We store our state (a State object).
            state = state_quadruple[2] 
            # If we haven't seen this state before, we can add it to our frontier.
            if str(state.state) not in self.was_seen:
                # We add the state triplet to our frontier.
                heapq.heappush(self.frontier, state_quadruple)
                self.max_nodes = max(self.max_nodes, len(self.frontier))

    # Making a move into the empty tile using the Misplaced Tiles heuristic.
    def make_move_using_mt(self):
        popped_state = None
        # As long as we have states to consider...
        while len(self.frontier) > 0:
            # We pop the state w/ the min cost. Recall that our quadruples are of the form (cost, id, state, moves).
            popped_state_quadruple = heapq.heappop(self.frontier)
            popped_state = popped_state_quadruple[2]
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
            self.moves = -1 # Setting the number of moves to -1 to indicate that the puzzle is unsolvable.
            return
        
        # If we've reached our goal state, we save some info and return.
        if popped_state.state == self.goal_state:
            self.current_state = popped_state
            self.moves = popped_state_quadruple[3]
            gn = popped_state.get_cost(popped_state_quadruple[3])
            hn = popped_state.get_heuristic_mt(self.goal_state)
            print(f"The final state w/ g(n)={gn} and h(n)={hn} is...")
            popped_state.print_state()
            return
        
        # The diameter of the puzzle is 31, so we can't have more than 31 moves.
        if popped_state_quadruple[3] > 31:
            print("The puzzle is unsolvable.")
            self.moves = -1 # Setting the number of moves to -1 to indicate that the puzzle is unsolvable.
            return
        
        # Some helpful text to let us know we're making progress.
        gn = popped_state.get_cost(popped_state_quadruple[3])
        hn = popped_state.get_heuristic_mt(self.goal_state)
        print(f"The best state to expand w/ g(n)={gn} and h(n)={hn} is...")
        popped_state.print_state()
        print()
        # Increment the number of nodes we've expanded.
        self.nodes_expanded += 1
        # Now, we can begin to process the popped state.
        self.current_state = popped_state
        # Storing the number of moves we've made to reach our current state.
        num_moves = popped_state_quadruple[3]
        self.moves = num_moves
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
            # Storing the number of moves we've made to reach our current state.
            num_moves = popped_state_quadruple[3]
            # We need a copy of the current state.
            current_state_copy = [row[:] for row in self.current_state.state]
            new_state = State(current_state_copy)
            # Swap the empty tile with the tile we want to move.
            new_state.state[empty_i][empty_j], new_state.state[i][j] = new_state.state[i][j], new_state.state[empty_i][empty_j]
            # For A* search w/ the MD heuristic, we consider the total cost of the state.
            num_moves += 1
            new_state_cost = new_state.get_total_cost_mt(num_moves, self.goal_state)
            # As we've produced a new state, we need to increment our state id.
            self.id += 1
            # We can then add the new state to our list of new states.
            new_states.append((new_state_cost, self.id, new_state, num_moves))
        
        # Next, we need to add the states we haven't seen to our frontier.
        # Recall that our quadruples are of the form (cost, id, state, moves).
        for state_quadruple in new_states:
            # We store our state (a State object).
            state = state_quadruple[2] 
            # If we haven't seen this state before, we can add it to our frontier.
            if str(state.state) not in self.was_seen:
                # We add the state triplet to our frontier.
                heapq.heappush(self.frontier, state_quadruple)
                self.max_nodes = max(self.max_nodes, len(self.frontier))

    # Making a move into the empty tile using the EUC heuristic.
    def make_move_using_euc(self):
        popped_state = None
        # As long as we have states to consider...
        while len(self.frontier) > 0:
            # We pop the state w/ the min cost. Recall that our quadruples are of the form (cost, id, state, moves).
            popped_state_quadruple = heapq.heappop(self.frontier)
            popped_state = popped_state_quadruple[2]
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
            self.moves = -1 # Setting the number of moves to -1 to indicate that the puzzle is unsolvable.
            return
        
        # If we've reached our goal state, we save some info and return.
        if popped_state.state == self.goal_state:
            self.current_state = popped_state
            self.moves = popped_state_quadruple[3]
            gn = popped_state.get_cost(popped_state_quadruple[3])
            hn = popped_state.get_heuristic_md(self.goal_state, self.tile_map)
            print(f"The final state w/ g(n)={gn} and h(n)={hn} is...")
            popped_state.print_state()
            return
        
        # The diameter of the puzzle is 31, so we can't have more than 31 moves.
        if popped_state_quadruple[3] > 31:
            print("The puzzle is unsolvable.")
            self.moves = -1 # Setting the number of moves to -1 to indicate that the puzzle is unsolvable.
            return

        # Some helpful text to let us know we're making progress.
        gn = popped_state.get_cost(popped_state_quadruple[3])
        hn = popped_state.get_heuristic_euc(self.goal_state, self.tile_map)
        print(f"The best state to expand w/ g(n)={gn} and h(n)={hn} is...")
        popped_state.print_state()
        print()
        # Increment the number of nodes we've expanded.
        self.nodes_expanded += 1
        # Now, we can begin to process the popped state.
        self.current_state = popped_state
        # Storing the number of moves we've made to reach our current state.
        num_moves = popped_state_quadruple[3]
        self.moves = num_moves
        # Get all the possible moves we can make from the current state.
        possible_moves = self.get_possible_moves()
        # Get the position of the empty tile.
        empty_tile_pos = self.get_empty_tile_pos()
        empty_i, empty_j = empty_tile_pos
        # A list to store the new states we can reach from the current state.
        new_states = []

        # Let's consider all the moves we can make.
        for move in possible_moves:
            i, j = move
            # Storing the number of moves we've made to reach our current state.
            num_moves = popped_state_quadruple[3]
            # We need a copy of the current state.
            current_state_copy = [row[:] for row in self.current_state.state]
            new_state = State(current_state_copy)
            # Swap the empty tile with the tile we want to move.
            new_state.state[empty_i][empty_j], new_state.state[i][j] = new_state.state[i][j], new_state.state[empty_i][empty_j]
            # For A* search w/ the EUC heuristic, we consider the total cost of the state.
            num_moves += 1
            new_state_cost = new_state.get_total_cost_euc(num_moves, self.goal_state, self.tile_map)
            # As we've produced a new state, we need to increment our state id.
            self.id += 1
            # We can then add the new state to our list of new states.
            new_states.append((new_state_cost, self.id, new_state, num_moves))

        # Next, we need to add the states we haven't seen to our frontier.
        # Recall that our quadruples are of the form (cost, id, state, moves).
        for state_quadruple in new_states:
            # We store our state (a State object).
            state = state_quadruple[2]
            # If we haven't seen this state before, we can add it to our frontier.
            if str(state.state) not in self.was_seen:
                # We add the state triplet to our frontier.
                heapq.heappush(self.frontier, state_quadruple)
                self.max_nodes = max(self.max_nodes, len(self.frontier))

    # Solve the problem using Uniform Cost Search.
    def solve_using_ucs(self):
        # Resetting the state id.
        self.id = 0
        # Defining our initial setup: the initial cost, the state id, the state itself, and the moves we've made.
        initial_cost = 0
        # Every quadruple in the heap is of the form (cost, id, state, moves).
        initial_setup = [(initial_cost, self.id, self.initial_state, 0)]
        heapq.heapify(initial_setup)
        # Our frontier is implemented as a min heap.
        self.frontier = initial_setup

        # We will begin processing the initial state.
        print("\nExpanding the initial state...")

        # As long as we haven't reached the goal state...
        while self.current_state.state != self.goal_state:
            # We make a move using Uniform Cost Search.
            self.make_move_using_ucs()
            # If the number of moves is -1, the puzzle is unsolvable.
            if self.moves == -1:
                print("The solution to this puzzle configuration is not possible.")
                return
        
        # Once we've reached the goal state, we've completed the puzzle using UCS.
        print()
        print("You have solved the puzzle!")
        print("Final State: ")
        self.print_current_state()
        print()
        # We print the number of nodes we've expanded, the max nodes in our frontier, and the depth of the goal node.
        # The number of nodes expanded must be offset by 1 because we increment it when processing the initial state.
        print(f"To solve this problem, UC search expanded a total of {self.nodes_expanded-1} nodes.")
        print(f"The maximum number of nodes in the frontier at any given time was: {self.max_nodes}")
        print("The depth of the goal node is: ", self.get_moves())
        print()

    # Solve the problem using the MD heuristic.
    def solve_using_md(self):
        # Resetting the state id.
        self.id = 0
        # Defining our initial setup: the initial cost, the state id, the state itself, and the moves we've made.
        initial_cost = 0
        # Every quadruple in the heap is of the form (cost, id, state, moves).
        initial_setup = [(initial_cost, self.id, self.initial_state, 0)]
        heapq.heapify(initial_setup)
        # Our frontier is implemented as a min heap.
        self.frontier = initial_setup

        # We will begin processing the initial state.
        print("\nExpanding the initial state...")

        # As long as we haven't reached the goal state...
        while self.current_state.state != self.goal_state:
            # We make a move using the MD heuristic.
            self.make_move_using_md()
            # If the number of moves is -1, the puzzle is unsolvable.
            if self.moves == -1:
                print("The solution to this puzzle configuration is not possible.")
                return

        # Once we've reached the goal state, we claim our VICTORY!
        print()
        print("You have solved the puzzle!")
        print("Final State: ")
        self.print_current_state()
        print()
        # We print the number of nodes we've expanded, the max nodes in our frontier, and the depth of the goal node.
        # The number of nodes expanded must be offset by 1 because we increment it when processing the initial state.
        print(f"To solve this problem, A* search w/ the MD heuristic expanded a total of {self.nodes_expanded-1} nodes.")
        print(f"The maximum number of nodes in the frontier at any given time was: {self.max_nodes}")
        print("The depth of the goal node is: ", self.get_moves())
        print()

    # Solve the problem using the Misplaced Tiles heuristic.
    def solve_using_mt(self):
        # Resetting the state id.
        self.id = 0
        # Defining our initial setup: the initial cost, the state id, the state itself, and the moves we've made.
        initial_cost = 0
        # Every quadruple in the heap is of the form (cost, id, state, moves).
        initial_setup = [(initial_cost, self.id, self.initial_state, 0)]
        heapq.heapify(initial_setup)
        # Our frontier is implemented as a min heap.
        self.frontier = initial_setup

        # We will begin processing the initial state.
        print("\nExpanding the initial state...")

        # As long as we haven't reached the goal state...
        while self.current_state.state != self.goal_state:
            # We make a move using the MT heuristic.
            self.make_move_using_mt()
            # If the number of moves is -1, the puzzle is unsolvable.
            if self.moves == -1:
                print("The solution to this puzzle configuration is not possible.")
                return

        # Once we've reached the goal state, we claim our VICTORY!
        print()
        print("You have solved the puzzle!")
        print("Final State: ")
        self.print_current_state()
        print()
        # We print the number of nodes we've expanded, the max nodes in our frontier, and the depth of the goal node.
        # The number of nodes expanded must be offset by 1 because we increment it when processing the initial state.
        print(f"To solve this problem, A* search w/ the MT heuristic expanded a total of {self.nodes_expanded-1} nodes.")
        print(f"The maximum number of nodes in the frontier at any given time was: {self.max_nodes}")
        print("The depth of the goal node is: ", self.get_moves())
        print()


    # Solve the problem using the EUC heuristic.
    def solve_using_euc(self):
        # Resetting the state id.
        self.id = 0
        # Defining our initial setup: the initial cost, the state id, the state itself, and the moves we've made.
        initial_cost = 0
        # Every quadruple in the heap is of the form (cost, id, state, moves).
        initial_setup = [(initial_cost, self.id, self.initial_state, 0)]
        heapq.heapify(initial_setup)
        # Our frontier is implemented as a min heap.
        self.frontier = initial_setup

        # We will begin processing the initial state.
        print("\nExpanding the initial state...")

        # As long as we haven't reached the goal state...
        while self.current_state.state != self.goal_state:
            # We make a move using the EUC heuristic.
            self.make_move_using_euc()
            # If the number of moves is -1, the puzzle is unsolvable.
            if self.moves == -1:
                print("The solution to this puzzle configuration is not possible.")
                return

        # Once we've reached the goal state, we claim our VICTORY!
        print()
        print("You have solved the puzzle!")
        print("Final State: ")
        self.print_current_state()
        print()
        # We print the number of nodes we've expanded, the max nodes in our frontier, and the depth of the goal node.
        # The number of nodes expanded must be offset by 1 because we increment it when processing the initial state.
        print(f"To solve this problem, A* search w/ the EUC heuristic expanded a total of {self.nodes_expanded-1} nodes.")
        print(f"The maximum number of nodes in the frontier at any given time was: {self.max_nodes}")
        print("The depth of the goal node is: ", self.get_moves())
        print()