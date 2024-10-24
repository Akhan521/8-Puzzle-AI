# Importing our State class from State.py.
from modules.State import State
from modules.Problem import Problem
import heapq

init_state = [[1,0,3], # A 0 represents the empty tile.
              [4,2,6],
              [7,5,8]]

goal_state = [[1,2,3],
              [4,5,6],
              [7,8,0]]

# Creating a State object with our initial state.
state = State(init_state)

# Creating a Problem object with our initial state and goal state.
problem = Problem(state, goal_state)

# Printing the initial state.
print("Initial State:")
problem.print_current_state()
print("Cost of our Initial State: ", problem.get_total_cost_mt())
print()

# Solving the 8 puzzle problem.
problem.solve_using_mt()
print("Number of Moves Taken: ", problem.num_moves)

