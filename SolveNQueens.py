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
             
    def n_queen(self, board, row, result_list):
        # base condition
        if row == len(board):
            # temp list to hold every ans in whole board
            temp_list = []
            # append it like string
            for i in range(len(board)):
                temp = ""
                for j in range(len(board[0])):
                    temp += board[i][j]
                temp_list.append(temp)
            #append the ans in every board
            result_list.append(temp_list)
            return
            
        # iterate til col
        for col in range(len(board[0])):
            if self.is_correct(board, row, col):
                board[row][col] = "Q"
                # call recursion in row
                self.n_queen(board, row+1, result_list)
                # back tracking
                board[row][col] = "."
    
    def solveNQueens(self,n):
        # create a board base on n nums
        board = []
        for i in range(n):
            list = []
            for j in range(n):
                list.append(".")
            board.append(list)
       # create list to hold a ans
        result_list = []     
        # create a methon that hold the board row and result    
        self.n_queen(board, 0, result_list)
        return result_list
    
# call the main method
solution = Solution()
ans = solution.solveNQueens(4)
for i in ans:
    print(i)