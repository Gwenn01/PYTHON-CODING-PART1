class Solution:   
    def is_correct(self, board, r, c):
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
             
    def n_queen(self, board, row):
        # base condition
        if row == len(board):
            return 1
        # iterate til col
        count = 0
        
        for col in range(len(board[0])):
            if self.is_correct(board, row, col):
                board[row][col] = "Q"
                # call recursion in row
                count += self.n_queen(board, row+1)
                # back tracking
                board[row][col] = "."
                
        return count
    
    def solveNQueens(self,n):
        # create a board base on n nums
        board = []
        for i in range(n):
            list = []
            for j in range(n):
                list.append(".")
            board.append(list)
                
        return self.n_queen(board, 0)
    
# call the main method
solution = Solution()
ans = solution.solveNQueens(4)
print(ans)