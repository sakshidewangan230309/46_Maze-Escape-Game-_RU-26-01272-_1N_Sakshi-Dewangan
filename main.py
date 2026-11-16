"""Maze Escape Game (PS No. - 46)
Console maze stored as a 2D list. Move with W/A/S/D, reach E to win.
Also finds the shortest path length from start to exit using BFS.
"""

from collections import deque

MAZE_TEMPLATE = [
    "P..##",
    "##.##",
    "#...#",
    "#.###",
    "#...E",
]

MOVES = {"W": (-1, 0), "S": (1, 0), "A": (0, -1), "D": (0, 1)}

def build_maze():
    maze = [list(row) for row in MAZE_TEMPLATE]
    start = exit_pos = None
    for r, row in enumerate(maze):
        for c, ch in enumerate(row):
            if ch == "P":
                start = (r, c)
                maze[r][c] = "."
            elif ch == "E":
                exit_pos = (r, c)
    return maze, start, exit_pos


def print_maze(maze, player):
    print()
    for r, row in enumerate(maze):
        print(" ". join("p" if (r, c) == player else ch for c, ch in enumerate(row)))
    print(f"Player position: (row {player[0]}, col {player[1]})")


def is_open(maze, r, c):
    return 0 <= r < len(maze) and 0 <= c < len(maze[0]) and maze[r][c] != "#"

def shortest_path_length(maze, start, exit_pos):
    queue = deque([(start, 0)])
    visited = {start}
    while queue:
        (r, c), dist = queue.popleft()
        if (r, c) == exit_pos:
            return dist
        for dr, dc in MOVES.values():
            nr, nc = r + dr, c + dc
            if is_open(maze, nr, nc) and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append(((nr, nc), dist + 1))
    return -1



def play(maze, start, exit_pos):
    player = start
    moves = 0
    print_maze(maze, player)
    while True:
        key = input("Move (W/A/S/D): ").strip().upper()
        if key not in MOVES:
            print(f"Invalid key '{key}'. Use W, A, S or D only.")
            continue
        dr, dc = MOVES[key]
        nr, nc = player[0] + dr, player[1] + dc
        if not is_open(maze, nr, nc):
            if not (0 <= nr < len(maze) and 0 <= nc < len(maze[0])):
                print(f"Cannot move outside the maze. Player stays at {player}.")
            else:
                print(f"Wall ahead. Move blocked. Player stays at {player}.")
            print(f"Moves counted: {moves}")
            print_maze(maze, player)
            continue
        player = (nr, nc)
        moves += 1
        print(f"Player moved to (row {nr}, col {nc}) | Moves: {moves}")
        print_maze(maze, player)
        if player == exit_pos:
            print(f"You escaped the maze! Total moves: {moves}")
            return


def main():
    while True:
        print("\n=== Maze Escape Game ===")
        print("1. Play Game")
        print("2. Show shortest path length")
        print("3. Quit")
        choice = input("Choose an option: ").strip()
        maze, start, exit_pos = build_maze()
        if choice == "1":
            play(maze, start, exit_pos)
        elif choice == "2":
            length = shortest_path_length(maze, start, exit_pos)
            if length < 0:
                print("No path to the exit.")
            else:
                print(f"Shortest Path length: {length} steps")
        elif choice == "3":
            print("Goodbye !")
            break 
        else:
            print("Invalid option. choose 1, 2 or 3.")

if __name__ == "__main__":
    main()

