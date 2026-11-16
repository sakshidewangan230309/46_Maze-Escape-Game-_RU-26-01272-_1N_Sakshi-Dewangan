A console maze game in **Python 3**. Move with **W/A/S/D** and reach the exit **E**. The program also finds the **shortest path** using **BFS**.

Made for B.Tech CSE (First Semester), Rungta International Skills University.

**Concepts used:** 2D lists, dictionary, tuples, loops, functions, BFS with a queue (`deque`)

---

## The Maze

```
P . . # #
# # . # #
# . . . #
# . # # #
# . . . E
```

| Symbol | Meaning |
|--------|---------|
| `P` | Player (starts at row 0, col 0) |
| `E` | Exit (row 4, col 4) |
| `#` | Wall |
| `.` | Open path |

---

## How to Run

```
python maze.py
```

Only Python 3 is needed. No extra libraries.

**Menu:** `1` Play Game, `2` Show shortest path length, `3` Quit

**Controls:** `W` up, `S` down, `A` left, `D` right (small letters also work)

---

## Requirements Followed

| # | Requirement | Where in my code |
|---|-------------|------------------|
| 1 | One `.py` file, runs in console | `maze.py` |
| 2 | Maze as 2D list, printed after every move | `build_maze()`, `print_maze()` |
| 3 | W/A/S/D moves, walls and outside blocked, not counted | `is_open()`, `play()` |
| 4 | Winning message with total moves | `play()` |
| 5 | BFS shortest path length | `shortest_path_length()` |

---

## Functions

| Function | What it does |
|----------|--------------|
| `build_maze()` | Turns the text maze into a 2D list, finds `start` and `exit_pos`, and returns all three. The `P` is replaced with `.` because the player is tracked by position. |
| `print_maze(maze, player)` | Prints the maze with `P` at the player's position, then prints `Player position: (row, col)`. |
| `is_open(maze, r, c)` | Returns `True` if the cell is inside the maze and not a wall. It checks the boundaries first to avoid an `IndexError`. |
| `shortest_path_length(maze, start, exit_pos)` | BFS: uses a queue and a `visited` set, checks 4 neighbours, and returns the distance when the exit is reached. Returns `-1` if there is no path. |
| `play(maze, start, exit_pos)` | Game loop. Takes a key, rejects invalid keys, blocks walls and outside moves (not counted), counts valid moves, and shows the win message at `E`. |
| `main()` | Shows the menu, builds a fresh maze each time, and calls `play()` or `shortest_path_length()`. |

**`MOVES` dictionary:** stores how each key changes the position as `(row, col)`:
`W = (-1, 0)`, `S = (1, 0)`, `A = (0, -1)`, `D = (0, 1)`

**Why BFS?** It checks all cells 1 step away, then 2 steps, and so on. So the first time it reaches the exit, that is the shortest path.

---

## Test Cases

| # | Input | Expected Output | Result |
|---|-------|-----------------|--------|
| 1 (Normal) | `D` | Player moved to (row 0, col 1), Moves: 1 | Passed |
| 2 (Boundary) | At (0, 0), press `W` | Cannot move outside the maze. Player stays at (0, 0). Moves: 0 | Passed |
| 3 (Invalid) | `D, D, D, X` | Wall ahead, move blocked at (0, 2). Invalid key 'X'. Moves counted: 2 | Passed |
| 4a (Valid) | `D, D, S, S, A, S, S, D, D, D` | You escaped the maze! Total moves: 10 | Passed |
| 4b (Valid) | Menu option 2 | Shortest path length: 10 steps | Passed |

**Path for Test Case 4:**
(0,0) → (0,1) → (0,2) → (1,2) → (2,2) → (2,1) → (3,1) → (4,1) → (4,2) → (4,3) → (4,4)

---

## Sample Output

```
Move (W/A/S/D): D
Player moved to (row 0, col 1) | Moves: 1

. P . # #
# # . # #
# . . . #
# . # # #
# . . . E
Player position: (row 0, col 1)
```

---

## What I Learned

- Storing a grid with a 2D list and using `maze[row][col]`
- Using a dictionary instead of many if/else statements
- How BFS finds the shortest path
- Handling invalid input so the program does not crash
- Splitting code into small functions

---

**Made by:** [Your Name] | **Roll No.:** [Your Roll No.]# 46_Maze-Escape-Game-_RU-26-01272-_1N_Sakshi-Dewangan
A Python-based Maze Escape Game with file handling.
