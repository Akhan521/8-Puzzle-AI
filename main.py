# Importing our State class from State.py.
from modules.State import State
from modules.Problem import Problem

init_state = [[1,0,3], # A 0 represents the empty tile.
              [4,2,6],
              [7,5,8]]

oh_boy = [[8,7,1],
          [6,0,2],
          [5,4,3]]

doable = [[0,1,2],
          [4,5,3],
          [7,8,6]]

easy = [[1,2,0],
        [4,5,3],
        [7,8,6]]

very_easy = [[1,2,3],
             [4,5,6],
             [7,0,8]]

trivial = [[1,2,3],
           [4,5,6],
           [7,8,0]]

goal_state = [[1,2,3],
              [4,5,6],
              [7,8,0]]

# Creating a State object with our initial state.
state = State(init_state)

# Creating a Problem object with our initial state and goal state.
problem = Problem(state, goal_state)

# Solving the 8 puzzle problem using UCS.
#problem.solve_using_ucs()

# Solving the 8 puzzle problem using A* w/ MT heuristic.
problem.solve_using_mt()

