# Importing our State class from State.py.
from modules.State import State
from modules.Problem import Problem

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
print("Total Cost: ", problem.get_total_cost_mt())
empty_tile_pos = problem.get_empty_tile_pos()
print("Empty Tile Position: ", empty_tile_pos)
poss_moves = problem.get_possible_moves()
print("Possible Moves: ", poss_moves)

problem.make_move()




