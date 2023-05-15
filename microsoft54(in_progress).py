"""
54. Spiral Matrix: https://leetcode.com/problems/spiral-matrix/

Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

# 12/25 Test Cases Passed:
class Solution(object):
    def spiralOrder(self, matrix):
        print("matrix: " ,matrix)
        if not matrix: 
            return []
        #:type matrix: List[List[int]]
        res = [] #:rtype: List[int]
        rows = len(matrix)
        cols = len(matrix[0])
        left = top = 0
        right = cols-1
        bottom = rows-1
        
        while len(res) < rows*cols:
            # Left to right top row:
            for i in range(left, right+1):
                res.append(matrix[top][i])
            top += 1 # move to 2nd row

            # Form Right Column:
            for i in range(top, bottom+1):
                res.append(matrix[i][right])
            right -= 1 # most right column completed
            # Use if to check for edge cases:
            # Right to left bottom row:`
            if top <= bottom:
                for i in range(right, left-1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1
            # Create most left column:
            if left <= right:
                for i in range(bottom, top-1, -1):
                    res.append(matrix[i][left])
                left+=1 # most left row completed
            return res
                
