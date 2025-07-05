# 8-Puzzle-AI: Solving the Classic 8-Puzzle Game Using AI Search Algos.

## 🧩 What is the 8-Puzzle Game?

The 8-Puzzle is a classic sliding tile puzzle made up of a 3×3 grid with **eight numbered tiles (1–8)** and **one empty space**. The challenge is to rearrange the tiles by sliding them one at a time into the empty space until all the tiles are in the correct order.

It typically begins with the tiles in a scrambled setup like this:

```
1 2 3  
4 0 6  
7 5 8  
```

And your objective is to reach the **goal state**:

```
1 2 3  
4 5 6  
7 8 0  
```

Where `0` represents the empty tile.

Each move slides a neighboring tile into the empty space, kind of like sliding puzzle pieces around without picking them up. While the rules are simple, solving it efficiently can be tricky, which is why I leverage AI to understand and test how computers make smart decisions, plan ahead, and find the best path to a goal.

---
## 🔍 AI Search Strategies Explained

This project solves the classic 8-Puzzle game using several intelligent search strategies from the field of artificial intelligence:

- **Uniform Cost Search (UCS):** Always expands the least-cost path first, like taking the most affordable step toward the solution.
- **A\* with Manhattan Distance:** Uses the number of moves (up, down, left, right) each tile is away from where it belongs (fast and highly effective).
- **A\* with Euclidean Distance:** Measures the straight-line distance from each tile’s current spot to its goal, good for estimating the shortest distance to the goal.
- **A\* with Misplaced Tiles:** Simply counts how many tiles are in the wrong place (quick and intuitive).

Built in Python, this solver highlights important AI concepts like search trees, heuristics (rules of thumb for guiding decisions), and how computers can find the most efficient path to a goal, all through the lens of a seemingly simple puzzle.

> ### 🧠 What Are Heuristics?
> In artificial intelligence, **heuristics** are smart rules or shortcuts that help guide decision-making. Instead of checking every possible move, a heuristic gives the solver a good guess about which options are closer to the goal. In the 8-Puzzle, this means prioritizing puzzle states that look more "solved," helping the AI find the solution faster and more efficiently.


### 💡  Side-by-Side Comparison

| Algorithm                     | Heuristic Used                 | Description                                                  |
|------------------------------|---------------------------------|--------------------------------------------------------------|
| Uniform Cost Search (UCS)    | None                            | Expands the path with the lowest cost so far                 |
| A* with Manhattan Distance   | Moves needed (up/down/left/right) | Fast, effective, and always finds the shortest path         |
| A* with Euclidean Distance   | Straight-line distance           | Estimates the most direct distance to the goal               |
| A* with Misplaced Tiles      | Number of wrong-position tiles  | Simple and quick, good for small puzzles                     |

---

## 🚀 Getting Started

Ready to solve the 8-Puzzle with AI? Follow these steps to run the project locally:

### ✅ Prerequisites
- Make sure you have **Python 3.8 or higher** installed  
  → [Download Python here](https://www.python.org/downloads/)

### 📦 1. Clone the Repository

Open your terminal or PowerShell and run:

```bash
git clone https://github.com/Akhan521/8-Puzzle-AI.git
cd 8-Puzzle-AI
```

### 🔧 2. (Optional but Recommended) Create a Virtual Environment

```bash
python -m venv venv
# Activate it:
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### ▶️ 3. Run the 8-Puzzle Solver

```bash
python main.py
```

---

## 💻 Example Run (Excluding Our Solution)

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

## ✨ Features

- Handles multiple preset/provided and custom puzzles
- Prints each state as it's expanded
- Tracks total nodes expanded, frontier size, and solution depth
- Modular design with customizable heuristics
- Optional and basic statistical analysis via `stats.py`

---

##  📚 Reflecting on Lessons Learned

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

## 📂 Project Structure

```
8-Puzzle-AI/
├── main.py               # Puzzle solver
├── stats.py              # Stats + optional visualizations
├── modules/
│   ├── State.py          # Represents puzzle state, heuristics
│   └── Problem.py        # Core search logic and algorithms
├── README.md             
└── .gitignore
```

---

## 👥 Authors

1. **Aamir Khan**  
 [LinkedIn](https://www.linkedin.com/in/aamir-khan-aak521/)  
 [GitHub](https://github.com/Akhan521)

2. **Abdi Nava**  
 [LinkedIn](https://www.linkedin.com/in/abdinava/)  
 [GitHub](https://github.com/abdinava)

---

## Supporting us!

If you found this interesting or useful, consider giving the repo a ⭐️ to show your support!

