def maze_path(p, row, col):
    #base condition
    if row == 1 and col == 1:
        print(p)
        return
    # take it or not, it should be 1to1
    # to reach the end
    if row > 1:
        maze_path(p + "D", row -1, col)
    if col > 1:
        maze_path(p + "R", row, col-1)

maze_path("", 3, 3)