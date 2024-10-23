# Importing our State class from State.py.
from State import State

# Creating a hardcoded state for testing purposes.

init_state = [[1,0,3], # A 0 represents the empty tile.
              [4,2,6],
              [7,5,8]]

cur_state = State(init_state)

cur_state.print_state()

