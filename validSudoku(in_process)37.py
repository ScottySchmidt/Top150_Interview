"""
36. Valid Sudoku: https://leetcode.com/problems/valid-sudoku/description/
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""

#NEED TO RETRY THIS PROBLEM AGAIN HAD TO LOOK UP EVERYTHONG
# A readable solution with average runTime:
class Solution(object):
    def isValidSudoku(self, board):
        
        # Take a list, compare set of nums to list. 
        # If set and list same length, then return True. All numbers are unique.
        def isValid(lst):
            numsList=[]
            for l in lst:
                if l=='.':
                    continue # need to ignore the .
                else:
                    numsList.append(l) 
            if len(numsList)==len(set(numsList)):
                return True
            else:
                 #print(numsList, " false found dup", set(numsList))
                 return False
            
        # Check each row:
        def checkRows(board):
            for row in board:
                #print(row, " ", type(row))
                if isValid(row) is False:
                    # print(row, " row found error", type(row))
                    return False
            return True
        
        # Check each column:
        def checkCols(board):
            for n in range(9):
                col = [c[n] for c in board]
                if isValid(col) is False:
                    #print(col, n,"  col found error")
                    return False
            return True
        
        # Check the 3 by 3 square:
        def checkBox(board):
            for r in (0, 3, 6):
                for c in (0, 3, 6):
                  box = [board[i][j] for j in range(c, c+3) for i in range(r, r+3)] # ChatGPT helped me with this complex line, I need futher thinking
                  print(box)
                  if isValid(box) is False:
                      return False
            return True

        return checkRows(board) and checkCols(board) and checkBox(board)
