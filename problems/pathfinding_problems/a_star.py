from data_structures.priority_queue import PriorityQueue

offsets = {
    "right": (0, 1),
    "left": (0, -1),
    "down": (1, 0),
    "up": (-1, 0)
}


def is_legal_pos(maze, neighbor):
    num_rows = len(maze)
    num_cols = len(maze[0])
    row, col = neighbor
    return 0 <= row < num_rows and 0 <= col < num_cols and neighbor != "*"


def get_path(predecessors, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = predecessors[current]
    path.append(start)
    path.reverse()
    return path


def heuristic(a, b):
    """
    Calculate the manhattan distance between two pairs of grid coordinates
    """
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)


def a_star(maze, start, goal):
    # create a PQ
    pq = PriorityQueue()
    # put the star in the PQ, the F-value will be 0
    # In this implementation, since there will be only one element in the PQ
    # the priority doesn't matter, so we are adding 0 as the F-value
    pq.put(start, 0)
    g_value = {
        start: 0
    }
    predecessors = {}
    # while the queue is not empty
    while not pq.is_empty():
        # get the item with highest priority
        current_cell = pq.get()
        # Is this the goal?
        if current_cell == goal:
            return get_path(predecessors, start, goal)
        # Otherwise add the undiscovered neighbors and calculate the F-value
        for direction in ["up", "right", "down", "left"]:
            row_offset, col_offset = offsets[direction]
            neighbor = (current_cell[0] + row_offset,
                        current_cell[1] + col_offset)
            if is_legal_pos(maze, neighbor) and neighbor not in g_value:
                # since each cell has a weight of 1 so we will add 1 to the
                # previous g value to calculate the g-value of the neighbor
                # (or the path from the start to the neighbor)
                new_cost = g_value[current_cell] + 1
                # update the g values for the neighbor
                g_value[neighbor] = new_cost
                f_value = new_cost + heuristic(goal, neighbor)
                pq.put(neighbor, f_value)
                predecessors[neighbor] = current_cell

    return None


if __name__ == "__main__":
    maze = [[0] * 3 for row in range(3)]
    start = (0, 0)
    goal = (2, 2)
    result = a_star(maze, start, goal)
    print(result)
