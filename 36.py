from collections import defaultdict

class Solution:
    def isValidSudoku(self, board):
        for row in range(9):
            dupe = set()
            
            for index in range(9):
                if board[row][index] == '.':
                    continue
                if board[row][index] in dupe:
                    return False
                else:
                    dupe.add(board[row][index])
        
        for col in range(9):
            dupe = set()
            
            for index in range(9):
                if board[index][col] == '.':
                    continue
                if board[index][col] in dupe:
                    return False
                else:
                    dupe.add(board[index][col])
        
        for square in range(9):
            dupe = set()
            
            for i in range(3):
                for j in range(3):
                    row = 3 * (square // 3) + i
                    col = 3 * (square % 3) + j
                    if board[row][col] == '.':
                        continue
                    if board[row][col] in dupe:
                        return False
                    else:
                        dupe.add(board[row][col])
        
        return True
        
obj = Solution()
board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

obj.isValidSudoku(board)