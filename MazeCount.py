def maze_count(row, col):
    if row == 1 or col == 1:
        return 1
    left = maze_count(row-1, col)
    right = maze_count(row, col-1)
    return left + right
    
ans = maze_count(3, 3)    
print(ans)