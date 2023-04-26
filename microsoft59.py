"""
Micorosft 59. Spiral Matrix II: https://leetcode.com/problems/spiral-matrix-ii/description/

Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

Example 1:
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
"""

# Original draft, works but messes up number 5:
class Solution(object):
    def generateMatrix(self, n):
        left = 0
        right = n
        top = 0
        end = n
        matrix = [ [0]*n for _ in range(3)]
        count=1

        while left <= right and top <= end:
            # Create first row:
            print("Going Right:")
            for row in range(left, right):
                matrix[top][row]=count
                count=count+1
                print(count)
            top=top+1 # top row complete
            
            # Create last column:
            print("Going Down:")
            for c in range(top, end):
                print(count)
                matrix[c][right-1]=count
                count=count+1
            right=right-1 # right col complete

            print("Going Left:")
            for row in range(right, left, -1):
                print(count)
                matrix[end-1][row]=count
                count=count+1
            end=end-1 # bottom row complete
            
            print("Going Up:")
            for c in range(end, top, -1):
                print(count)
                matrix[c][left]=count
                count=count+1
            left=left+1
            
        return matrix
