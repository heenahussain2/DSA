from data_structures.queue_ds import Queue


offset = {
    "right": (0, 1),  # add one column
    "left": (0, -1),  # subtract one column
    "up": (-1, 0),  # subtract one row
    "down": (1, 0)  # add one row
}


def get_path(predecessors, start, goal):
    path = []
    current_node = goal
    while current_node != start:
        path.append(current_node)
        current_node = predecessors[current_node]
    path.append(start)
    path.reverse()
    return path


def is_legal_pos(neighbor, maze):
    num_rows = len(maze)
    num_cols = len(maze[0])
    row, col = neighbor
    return 0 <= row < num_rows and 0 <= col < num_cols and \
        maze[row][col] != "*"


def bfs(maze, start, goal):
    queue = Queue()
    predecessors = {}
    # 1. Enqueue the starting node
    queue.enqueue(start)
    predecessors[start] = None
    # 2. While the queue is not empty
    while not queue.is_empty():
        # 3. Dequeue
        current_node = queue.dequeue()
        # 4. If the current node is the goal, return the path
        if current_node == goal:
            return get_path(predecessors, start, goal)
        # 5. enqueue undiscovered neighbors (neighbor should not
        # be in predecessors)
        for direction in ["up", "right", "down", "left"]:
            row_offset, col_offset = offset[direction]
            neighbor = (current_node[0] + row_offset,
                        current_node[1] + col_offset)
            if is_legal_pos(neighbor, maze) and neighbor not in predecessors:
                queue.enqueue(neighbor)
                # Add predecessor for neighbors
                predecessors[neighbor] = current_node
    return None


if __name__ == "__main__":
    # First maze
    maze = [[0] * 3 for row in range(3)]
    start = (0, 0)
    goal = (2, 2)
    result = bfs(maze, start, goal)
    print(result)
