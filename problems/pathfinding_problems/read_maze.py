def read_maze(file_path):
    try:
        with open(file_path) as fh:
            maze = [[char for char in line.strip("\n")] for line in fh]
            first_row_len = len(maze[0])
            # check if all the rows have same length
            for row in maze:
                if len(row) != first_row_len:
                    print("The maze is not of equal length")
                    raise SystemExit
            return maze
    except OSError:
        print("There is a problem with the selected file")
        raise SystemExit


if __name__ == "__main__":
    file_name = "challenge_maze.txt"
    maze_file = f"data_structures/problems/2DList_problems/mazes/{file_name}"
    maze = read_maze(maze_file)
    for row in maze:
        print(row)
