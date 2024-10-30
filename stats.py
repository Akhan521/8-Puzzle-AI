# Importing our classes.
from modules.State import State
from modules.Problem import Problem
import pandas as pd

# Importing matplotlib for plotting.
import matplotlib.pyplot as plt

# Different initial states for the 8 puzzle problem: ( A 0 represents the empty tile )
init_state = [[1,0,3],
              [4,2,6],
              [7,5,8]]

trivial = [[1,2,3],
           [4,5,6],
           [7,8,0]]

very_easy = [[1,2,3],
             [4,5,6],
             [7,0,8]]

easy = [[1,2,0],
        [4,5,3],
        [7,8,6]]

doable = [[0,1,2],
          [4,5,3],
          [7,8,6]]

oh_boy = [[8,7,1],
          [6,0,2],
          [5,4,3]]

impossible = [[1,2,3],
              [4,5,6],
              [8,7,0]]

goal_state = [[1,2,3],
              [4,5,6],
              [7,8,0]]

all_states = [trivial, very_easy, easy, doable, oh_boy, impossible]
#algorithms = ['Uniform Cost Search', 'Misplaced Tiles Heuristic', 'Euclidean Distance Heuristic']

# List to store the number of nodes expanded per algorithm.
ucs_expanded = []
mt_expanded = []
euc_expanded = []
md_expanded = []

# List to store the max number of nodes in the frontier per algorithm.
ucs_max_frontier = []
mt_max_frontier = []
euc_max_frontier = []
md_max_frontier = []

# Solving the 8 puzzle problem for all states.
for state in all_states:
        # Creating a state object.
        state = State(state)
        
        # Running the Uniform Cost Search algorithm.
        problem1 = Problem(state, goal_state)
        problem1.solve_using_ucs()
        ucs_expanded.append(problem1.nodes_expanded)
        ucs_max_frontier.append(problem1.max_nodes)
        

        # Running the Misplaced Tiles algorithm.
        problem2 = Problem(state, goal_state)
        problem2.solve_using_mt()
        mt_expanded.append(problem2.nodes_expanded)
        mt_max_frontier.append(problem2.max_nodes)
        

        # Running the Euclidean Distance algorithm.
        problem3 = Problem(state, goal_state)
        problem3.solve_using_euc()
        euc_expanded.append(problem3.nodes_expanded)
        euc_max_frontier.append(problem3.max_nodes)
        

        # Running the Manhattan Distance algorithm.
        problem4 = Problem(state, goal_state)
        problem4.solve_using_md()
        md_expanded.append(problem4.nodes_expanded)
        md_max_frontier.append(problem4.max_nodes)
        

# Plotting the nodes expanded per puzzle to compare the search algorithms.
puzzle_diffs = ['Trivial', 'Very Easy', 'Easy', 'Doable', 'Oh Boy', 'Impossible']

# plt.figure(figsize=(10, 6))

# plt.plot(puzzle_diffs, ucs_expanded, marker='o', label='Uniform Cost Search')
# plt.plot(puzzle_diffs, mt_expanded, marker='o', label='Misplaced Tiles')
# plt.plot(puzzle_diffs, euc_expanded, marker='o', label='Euclidean Distance')
# plt.plot(puzzle_diffs, md_expanded, marker='o', label='Manhattan Distance')

# plt.xlabel('Puzzle Difficulty')
# plt.ylabel('Number of Nodes Expanded')
# plt.title('Number of Nodes Expanded Per Algorithm')
# plt.legend()
# plt.grid(True)
# plt.show()

# Plotting the maximum queue size per puzzle to compare the search algorithms.
# plt.figure(figsize=(10, 6))

# plt.plot(puzzle_diffs, ucs_max_frontier, marker='o', label='Uniform Cost Search')
# plt.plot(puzzle_diffs, mt_max_frontier, marker='o', label='Misplaced Tiles')
# plt.plot(puzzle_diffs, euc_max_frontier, marker='o', label='Euclidean Distance')
# plt.plot(puzzle_diffs, md_max_frontier, marker='o', label='Manhattan Distance')

# plt.xlabel('Puzzle Difficulty')
# plt.ylabel('Maximum Queue Size')
# plt.title('Maximum Queue Size Per Algorithm')
# plt.legend()
# plt.grid(True)
# plt.show()

# # Making a table out of our data for nodes expanded per algorithm.
# data = {
#         'Puzzle Difficulty': ['Trivial', 'Very Easy', 'Easy', 'Doable', 'Oh Boy', 'Impossible'],
#         'Uniform Cost Search': ucs_expanded,
#         'Misplaced Tiles': mt_expanded,
#         'Euclidean Distance': euc_expanded,
#         'Manhattan Distance': md_expanded
# }

# df = pd.DataFrame(data)

# # Printing the DataFrame.
# print('\n\n')
# print("Number of Nodes Expanded Per Algorithm")
# print('---------------------------------------------------------------------------------------')
# print(df)

# data = {
#         'Puzzle Difficulty': ['Trivial', 'Very Easy', 'Easy', 'Doable', 'Oh Boy', 'Impossible'],
#         'Uniform Cost Search': ucs_max_frontier,
#         'Misplaced Tiles': mt_max_frontier,
#         'Euclidean Distance': euc_max_frontier,
#         'Manhattan Distance': md_max_frontier
# }

# df = pd.DataFrame(data)

# # Printing the DataFrame.
# print('\n\n')
# print("Maximum Queue Size Per Puzzle")
# print('---------------------------------------------------------------------------------------')
# print(df)