class Solution:
    def display(self, board):
        for boards in board:
            print(boards)
        
    def is_safe(self, board, row, col, num):
        #check row
        for i in range(len(board)):
            if board[i][col] == num:
                return False
         #check col
        for i in range(len(board[0])):
             if board[row][i] == num:
                 return False
         # check 3x3 box"
        start_row = row - row % 3
        start_col = col - col % 3
        for i in range(start_row, start_row + 3):
             for j in range(start_col, start_col + 3):
                 if board[i][j] == num:
                     return False                     
        return True             
        
        
    def solve(self, board):
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == '.':
                    for num in range(1, 10):
                        num = str(num)
                        if self.is_safe(board, row, col, num):
                            board[row][col] = num
                            if self.solve(board):
                                return True
                            # backtracking 
                            board[row][col] = '.'
                    # if we check till 10 and nothing fit then return false to backtract      
                    return False
        self.display(board)
        # if we fill all the board return true,to go into above     
        return True                    
        
# execute the code
solution = Solution()       
board = [["5","3",".",".","7",".",".",".","."],
              ["6",".",".","1","9","5",".",".","."],
              [".","9","8",".",".",".",".","6","."],
              ["8",".",".",".","6",".",".",".","3"],
              ["4",".",".","8",".","3",".",".","1"],
              ["7",".",".",".","2",".",".",".","6"],
              [".","6",".",".",".",".","2","8","."],
              [".",".",".","4","1","9",".",".","5"],
              [".",".",".",".","8",".",".","7","9"]
]
ans = solution.solve(board)
print(ans)
