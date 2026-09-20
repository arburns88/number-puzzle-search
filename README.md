# Sliding Tile Puzzle Solver — BFS, DLS, IDS

Project 1 for CS 381 (Intro to AI), Fall 2026. Implements and compares three uninformed tree-search algorithms — Breadth-First Search, Depth-Limited Search, and Iterative Deepening Search — on the classic 4x4 sliding tile puzzle.

## Algorithms

- **BFS** — guaranteed optimal solution, but memory grows exponentially with depth
- **DLS** — DFS bounded to a fixed depth limit; fast and low-memory, but may miss the optimal solution
- **IDS** — repeated DLS calls with increasing depth limits; optimal like BFS, but with DLS's linear memory footprint

All three use **tree search**: there is no general visited-set — the only excluded successor is the immediate parent state.

## Input format

States are 4x4 grids given as a vector of 4 vectors, with `0` as the blank:
[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
## Usage

```bash
python puzzle_solver.py
```

The program prompts for:
1. Start state
2. Goal state
3. Algorithm — `(1)` BFS, `(2)` IDS, `(3)` BFS and IDS, `(4)` DLS

## Output

- Solution (or failure)
- Number of moves and the move sequence (over `{L, R, U, D}`)
- Number of states removed from the queue/stack
- Maximum queue/stack size
- CPU time

## Team

- Adam Burns
- Daniel Ariaz-Avalos
