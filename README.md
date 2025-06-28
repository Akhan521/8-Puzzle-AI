# 8-Puzzle-AI: Solving the Classic 8-Puzzle Game Using AI Search Algos.

This project solves the classic 8-Puzzle game using a variety of AI search algorithms:
- **Uniform Cost Search (UCS)**
- **A\* Search with the Manhattan Distance heuristic**
- **A\* Search with the Euclidean Distance heuristic**
- **A\* Search with the Misplaced Tiles heuristic**

Built in Python, this 8-Puzzle solver demonstrates core concepts in AI including state-space search, admissible heuristics, and optimal pathfinding.

---

## What is the 8-Puzzle Game?

The 8-Puzzle is a sliding puzzle game, with 8 numbered square tiles and one empty space. The goal is to reach the goal state seen below by sliding the tiles around strategically.

**Goal State:**
```
1 2 3
4 5 6
7 8 0
```
Where `0` represents the empty tile.

---

## Search Algorithms Implemented

| Algorithm                     | Heuristic Used             | Description                                                  |
|------------------------------|-----------------------------|--------------------------------------------------------------|
| Uniform Cost Search (UCS)    | None                        | Expands nodes based only on path cost `g(n)`                 |
| A* with Manhattan Distance   | Sum of vertical + horizontal distances | Optimal and efficient in practice                            |
| A* with Euclidean Distance   | Straight-line (geometric) distance       | Good spatial approximation                                   |
| A* with Misplaced Tiles      | Number of misplaced tiles   | Simple but effective in many cases                           |

---

## Getting Started / Running the Project

### 1. Clone the Repository
```bash
git clone https://github.com/Akhan521/8-Puzzle-AI.git
cd 8-Puzzle-AI
```

### 2. Run the 8-Puzzle Solver
```bash
python main.py
```

---

## 💻 Example Run

```
Welcome to our 8-puzzle solver.
Type '1' to use a default puzzle, or '2' to enter your own puzzle.
Your choice: 2

Enter your puzzle, use a zero to represent the blank.
Enter the first row, use spaces or tabs between numbers: 1 2 3
Enter the second row, use spaces or tabs between numbers: 4 5 6
Enter the third row, use spaces or tabs between numbers: 7 0 8

Enter your algorithm of choice:
1. Uniform Cost Search
2. A* with the Manhattan Distance Heuristic
3. A* with the Euclidean Distance Heuristic
4. A* with the Misplaced Tiles Heuristic
Your choice: 2
```

---

## Features

- Handles multiple preset/provided and custom puzzles
- Prints each state as it's expanded
- Tracks total nodes expanded, frontier size, and solution depth
- Modular design with customizable heuristics
- Optional and basic statistical analysis via `stats.py`

---

## Reflecting on Lessons Learned

This project helped us apply and internalize several core concepts in AI and software engineering:

### Algorithmic Thinking
- Implemented UCS and multiple A\* variations from scratch
- Designed and tested admissible heuristics (Manhattan, Euclidean, Misplaced Tiles)
- Tuned performance by comparing node expansion and depth across strategies

### Heuristics & Optimization
- Gained intuition on how the heuristic choice/quality affects algorithm efficiency
- Observed differences in path cost and explored trade-offs

### Software Design
- Practiced modular Python design with OOP principles
- Built reusable components like `State`, `Problem`, and a consistent CLI interface
- Used Python’s `heapq` for efficient frontier management

### Debugging & Analysis
- Handled edge cases like unsolvable puzzles and goal-state detection
- Implemented basic statistical analysis to visualize and compare algorithms

---

## Project Structure

```
8-Puzzle-AI/
├── main.py               # Puzzle solver
├── stats.py              # Stats + optional visualizations
├── modules/
│   ├── State.py          # Represents puzzle state, heuristics
│   └── Problem.py        # Core search logic and algorithms
├── README.md             # This file
└── .gitignore
```

---

## Authors

1. **Aamir Khan**  
 [LinkedIn](https://www.linkedin.com/in/aamir-khan-bb83b8235)  
 [GitHub](https://github.com/Akhan521)

2. **Abdi Nava**  
 [LinkedIn](https://www.linkedin.com/in/abdinava/)  
 [GitHub](https://github.com/abdinava)

---

## Supporting us!

If you found this interesting or useful, consider giving the repo a ⭐️ to show your support!

