def maze_path(p, row, col):
    # base condition
    if row == 1 and col == 1:
        print(p)
        return
   # if we see a path restrictions 
   # just return
    if row == 2 and col == 2:
        return
    #call recursion call
    if row > 1:
        maze_path(p + "D", row -1, col)
    if col > 1:
        maze_path(p + "R", row, col-1)
        
maze_path("", 3, 3)            