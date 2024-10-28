# Importing our State class from State.py.
from modules.State import State
from modules.Problem import Problem

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

goal_state = [[1,2,3],
              [4,5,6],
              [7,8,0]]

print("Welcome to 862400489's and 862425795's 8 puzzle solver.")
option = input("Type '1' to use a default puzzle, or '2' to enter your own puzzle.\n")

if option == '2':
    print("Enter your puzzle, use a zero to represent the blank.")
    row_1 = input("Enter the first row, use spaces or tabs between numbers: ")
    row_1 = [int(item) for item in row_1.split()]
    row_2 = input("Enter the second row, use spaces or tabs between numbers: ")
    row_2 = [int(item) for item in row_2.split()]
    row_3 = input("Enter the third row, use spaces or tabs between numbers: ")
    row_3 = [int(item) for item in row_3.split()]

    puzzle = [row_1, row_2, row_3]
    print("\nEnter your algorithm of choice:")
    print("1. Uniform Cost Search")
    print("2. A* with the Manhattan Distance Heuristic")
    print("3. A* with the Euclidean Distance Heuristic")
    choice = input("\nYour choice: ")

    state = State(puzzle)
    problem = Problem(state, goal_state)

    if choice == '1':
        problem.solve_using_ucs()
    elif choice == '2':
        problem.solve_using_mt()
    elif choice == '3':
        problem.solve_using_euc()
else:
    # Creating a State object with our initial state.
    state = State(init_state)

    # Creating a Problem object with our initial state and goal state.
    problem = Problem(state, goal_state)

    # Solving the 8 puzzle problem using UCS.
    #problem.solve_using_ucs()

    # Solving the 8 puzzle problem using A* w/ MT heuristic.
    #problem.solve_using_mt()

    # Solving the 8 puzzle problem using EUC
    problem.solve_using_euc()
