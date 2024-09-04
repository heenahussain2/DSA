# import read_maze
from data_structures.stack import Stack


offset = {
    "right": (0, 1),  # add one column
    "left": (0, -1),  # subtract one column
    "up": (-1, 0),  # subtract one row
    "down": (1, 0)  # add one row
}


def get_path(predecessors, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = predecessors[current]
    path.append(start)
    path.reverse()
    return path


def is_legal_pos(maze, pos):
    i, j = pos
    num_rows = len(maze)
    num_cols = len(maze[0])

    return 0 <= i < num_rows and 0 <= j < num_cols and maze[i][j] != "*"


def dfs(maze, start, goal):
    # 1. create a stack
    stack = Stack()
    # 2. push the start position to the stack
    stack.push(start)
    predecessors = {
        start: None
    }
    while not stack.is_empty():
        current_cell = stack.pop()
        if current_cell == goal:
            return get_path(predecessors, start, goal)

        for direction in ["up", "right", "down", "left"]:
            row_offset, col_offset = offset[direction]
            neighbour = (row_offset + current_cell[0],
                         col_offset + current_cell[1])
            # if the position exists in the maze, and the cell is undiscovered
            if is_legal_pos(maze, neighbour) and neighbour not in predecessors:
                # add the neighbour to stack
                stack.push(neighbour)
                # add neighbour to predecessor
                predecessors[neighbour] = current_cell

        return None


if __name__ == "__main__":
    # First maze
    maze = [[0] * 3 for row in range(3)]
    start = (0, 0)
    goal = (2, 2)
    result = dfs(maze, start, goal)
    print(result)
