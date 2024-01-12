"""
73. Set Matrix Zeroes: https://leetcode.com/problems/set-matrix-zeroes/description/
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 
Follow up:
A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""

# Brute force solution beats 10%, how to do this in O(m + n) space?
class Solution(object):
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        row = []
        col = []
        
        for x in range(m):
            for y in range(n):
                if matrix[x][y]==0:
                    row.append(x)
                    col.append(y)
            
        for x in range(m):
            for y in range(n):
                if x in row or y in col:
                    matrix[x][y]=0
        return matrix
