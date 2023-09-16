class Solution:
    def is_duplicate(self, board, row, col):
        #append every value in row, col and box in a list, then check it if there is a duplicate using set dsa
        #row duplicate
        temp_row = []
        for i in range(len(board)):
            if board[i][col] != '.':
                temp_row.append(int(board[i][col]))
        if len(temp_row) != len(set(temp_row)):
            return True
        #col duplicate
        temp_col = []
        for i in range(len(board[0])):
             if board[row][i] != '.':
                 temp_col.append(int(board[row][i]))
        if len(temp_col) != len(set(temp_col)):
         return True
         #3x3 box duplicate
        temp_box = []
        start_row = row - row % 3
        start_col = col - col % 3
        for i in range(start_row, start_row + 3):
             for j in range(start_col, start_col + 3):
                 if board[i][j] != '.':
                     temp_box.append(int(board[i][j]))
        if len(temp_box) != len(set(temp_box)):
         return True
        
         # if not duplicate, return false
        return False          
        
    def is_valid_sudoku(self, board):
        for row in range(len(board)):
            for col in range(len(board[0])):
                if self.is_duplicate(board, row, col):
                    return False
        return True
        
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
ans = solution.is_valid_sudoku(board)
print(ans)