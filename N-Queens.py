def is_correct(board, r, c):
    # check the up
    row = r - 1
    col = c
    while row >= 0:
        if board[row][col] == 'Q':
            return False
        row -= 1
    # check left side
    row = r -1
    col = c - 1
    while row >= 0 and col >= 0:
        if board[row][col] == 'Q':
            return False
        col -= 1
        row -= 1
   # check right side
    row = r - 1
    col = c + 1
    while row >= 0 and col <= len(board[0])-1:
         if board[row][col] == 'Q':
             return False
         col += 1
         row -= 1
   # return true not found
    return True
                
def n_queen(board, row):
    # base condition
    if row == len(board):
        for boards in board:
            print(boards)
        print()
        return
    # iterate til col
    for col in range(len(board[0])):
        if is_correct(board, row, col):
            board[row][col] = "Q"
            # call recursion in row
            n_queen(board, row+1)
            # back tracking
            board[row][col] = " "
       
        
board = [
               [" ", " ", " ", " "],
               [" ", " ", " ", " "],
               [" ", " ", " ", " "],
               [" ", " ", " ", " "]
]
n_queen(board, 0)