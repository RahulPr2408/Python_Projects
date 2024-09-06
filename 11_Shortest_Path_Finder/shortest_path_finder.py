import curses
from curses import wrapper
import queue
import time
import heapq

maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]

def print_maze(maze, stdscr, path=[]):
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)
    GREEN = curses.color_pair(3)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:
                if (i, j) == path[0]:  # Start point
                    stdscr.addstr(i, j*2, "O", GREEN)
                elif (i, j) == path[-1]:  # End point
                    stdscr.addstr(i, j*2, "X", RED)
                else:
                    stdscr.addstr(i, j*2, "X", RED)
            else:
                stdscr.addstr(i, j*2, value, BLUE)

def find_start(maze, start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j
    return None

def find_neighbors(maze, row, col):
    neighbors = []
    if row > 0:  # UP
        neighbors.append((row - 1, col))
    if row + 1 < len(maze):  # DOWN
        neighbors.append((row + 1, col))
    if col > 0:  # LEFT
        neighbors.append((row, col - 1))
    if col + 1 < len(maze[0]):  # RIGHT
        neighbors.append((row, col + 1))
    return neighbors

# BFS Algorithm
def bfs(maze, stdscr):
    start = "O"
    end = "X"
    start_pos = find_start(maze, start)

    q = queue.Queue()
    q.put((start_pos, [start_pos]))

    visited = set()

    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos

        stdscr.clear()
        print_maze(maze, stdscr, path)
        time.sleep(0.2)
        stdscr.refresh()

        if maze[row][col] == end:
            return path

        neighbors = find_neighbors(maze, row, col)
        for neighbor in neighbors:
            if neighbor in visited:
                continue

            r, c = neighbor
            if maze[r][c] == "#":
                continue

            new_path = path + [neighbor]
            q.put((neighbor, new_path))
            visited.add(neighbor)

# A* Algorithm
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(maze, stdscr):
    start = find_start(maze, 'O')
    end = find_start(maze, 'X')

    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}

    visited = set()

    while open_set:
        current = heapq.heappop(open_set)[1]

        stdscr.clear()
        print_maze(maze, stdscr, list(came_from.values()))
        stdscr.refresh()
        time.sleep(0.2)

        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        visited.add(current)

        for neighbor in find_neighbors(maze, current[0], current[1]):
            if neighbor in visited or maze[neighbor[0]][neighbor[1]] == '#':
                continue

            tentative_g_score = g_score[current] + 1

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

# Interactive menu
def menu(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Choose an Algorithm:")
    stdscr.addstr(1, 0, "1. Breadth-First Search (BFS)")
    stdscr.addstr(2, 0, "2. A* Search")
    stdscr.addstr(4, 0, "Press 'q' to quit.")
    stdscr.refresh()

    key = stdscr.getch()
    if key == ord('1'):
        return 'BFS'
    elif key == ord('2'):
        return 'A*'
    elif key == ord('q'):
        return 'QUIT'

def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)

    while True:
        algorithm_choice = menu(stdscr)
        
        if algorithm_choice == 'QUIT':
            break

        start_time = time.time()

        if algorithm_choice == 'BFS':
            path = bfs(maze, stdscr)
        elif algorithm_choice == 'A*':
            path = a_star(maze, stdscr)

        end_time = time.time()
        
        stdscr.clear()
        if path:
            print_maze(maze, stdscr, path)
            stdscr.addstr(len(maze) + 1, 0, f"Path found using {algorithm_choice} in {end_time - start_time:.2f} seconds!", curses.color_pair(2))
        else:
            stdscr.addstr(len(maze) + 1, 0, "No path found.", curses.color_pair(2))

        stdscr.addstr(len(maze) + 2, 0, "Press any key to continue...")
        stdscr.getch()

wrapper(main)
