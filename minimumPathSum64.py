"""
64. Minimum Path Sum, Google https://leetcode.com/problems/minimum-path-sum/

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.

Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12
"""

# Final Accepted Solution but could use improved runtime:
class Solution(object):
    def minPathSum(self, grid):
        import numpy as np
        # print("original: ", grid)
        m = len(grid)
        n = len(grid[0])
        copy = np.zeros((m, n)) #Create copy of original grid
        copy[0][0] = grid[0][0] # set first num to original grid
        
        # first row accumulative sum:
        for i in range(1, n):
            #New Next    =   Prev  +  original num
            copy[0][i]=copy[0][i-1] + grid[0][i]
        
        # first col accumlative sum:
        for j in range(1, m):
             #Next Col    = prev col  + original num 
             copy[j][0] = copy[j-1][0] + grid[j][0]

        # rest of grid, row, col:
        for i in range(1, m):
            for j in range(1, n):
                #new num  = min(above or left) + original num
                copy[i][j] = min(copy[i-1][j], copy[i][j-1]) + grid[i][j]  
        #print(copy)
        return int(copy[-1][-1])


# Current draft is close with small bug:
class Solution(object):
    def minPathSum(self, grid):
        import numpy as np
        print("original: ", grid)

        rows = len(grid)
        cols = len(grid[0])

        copy = np.zeros((rows, cols)) #Create copy of original grid
        copy[0][0] = grid[0][0] # set first num to original grid
        
        # first row accumulative sum:
        for i in range(1, rows):
            #New Next    =   Prev  +  original num
            copy[0][i]=copy[0][i-1] + grid[0][i]
        
        # first col accumlative sum:
        for j in range(1, cols):
             #Next Col    = prev col  + original num 
             copy[j][0] = copy[j-1][0] + grid[j][0]

        # rest of grid, row, col:
        for i in range(1, rows):
            for j in range(1, cols):
                #new num  = min(above or left) + original num
                copy[j][i] = min(copy[j-1][i], copy[j][i-1]) + grid[j][i]  
        #print(copy)
        return copy[-1][-1]
