def path_all(maze, p, row, col, index):
    # base condition
    if row == len(maze)-1 and col == len(maze[0])-1:
        maze[row][col] = index
        index += 1
        for mazes in maze:
            print(mazes)
        print(p)
        return
    #if maze alredy mark, then return
    if maze[row][col] != 0:
        return
    # back tracking
    maze[row][col] = index
    index += 1
    # recursion call
    if row < len(maze)-1:
        path_all(maze, p + "D", row+1, col, index)
    if col < len(maze)-1:
        path_all(maze, p + "R", row, col+1, index)
    if row > 0:
        path_all(maze, p + "U", row-1, col, index)
    if col > 0:
        path_all(maze, p + "L", row, col-1, index)
    # bring back the backtracking
    index -= 1
    maze[row][col] = 0   
    
maze = [
              [0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]
]
path_all(maze, "", 0, 0, 1)