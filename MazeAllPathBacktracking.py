# Path all maze U, D, L, R
# Backtracking
def path_all(maze, p, row, col):
    #base condition we meet the ans
    if row == len(maze)-1 and col == len(maze)-1:
        print(p)
        return
    #if maze already mark, we cant go back
    if not maze[row][col]:
        return
    # back track every recursion
    maze[row][col] = False
    # recursion call
    if row < len(maze)-1:
        path_all(maze, p + "D", row+1, col)
    if col < len(maze)-1:
        path_all(maze, p + "R", row, col+1)
    if row > 0:
        path_all(maze, p + "U", row-1, col)
    if col > 0:
        path_all(maze, p + "L", row, col-1)
    # remove and back track 
    maze[row][col] = True
    
maze = [
    [True, True, True],
    [True, True, True],
    [True, True, True]
]
path_all(maze, "", 0, 0)