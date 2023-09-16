def maze_path(p, row, col):
    #base condition
    if row == 1 and col == 1:
        list = []
        list.append(p)
        return list
    # take it or not, it should be 1to1
    # to reach the end
    list = []
    if row > 1 and col > 1:
         list.extend(maze_path(p + "D", row -1, col-1))
    if row > 1:
        list.extend(maze_path(p + "V", row -1, col))
    if col > 1:
        list.extend(maze_path(p + "H", row, col-1))
    
    return list
    
print(maze_path("", 3, 3))