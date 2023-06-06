"""
62. Unique Paths: https://leetcode.com/problems/unique-paths/description/   Medium Google Interview Practice

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
The robot can only move either down or right at any point in time.
Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
The test cases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:
Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
"""

# This problem has to have the math knowledge to understand. 
# I created comments on how this solution works, but would struggle to recreate from memory, would need practice:
# See output comments at end to see how this problem runs:
class Solution(object):
    def uniquePaths(self, m, n):
        row = [1] * n  # [1, 1, 1, 1, 1, 1, 1] # Last row is always 1 for each length

        for col in range(m-1):  # Always create one less new row for height of grid
            newRow = [1] * n # Create empty row
            for i in range(n-2, -1, -1): # going backwards by 1. 
            # start at n-2 since first one higher index from newRow[i+1] below would get index error
                newRow[i] = newRow[i+1] + row[i] # last of cur row plus last of last list
                print(newRow[i], " = ", newRow[i+1], " plus", row[i])
            row = newRow # update latest row
            print(row, " updated row")

        return row[0] # first num in list should be final answer
"""
(2, ' = ', 1, ' plus', 1)
(3, ' = ', 2, ' plus', 1)
(4, ' = ', 3, ' plus', 1)
(5, ' = ', 4, ' plus', 1)
(6, ' = ', 5, ' plus', 1)
(7, ' = ', 6, ' plus', 1)
([7, 6, 5, 4, 3, 2, 1], ' updated row')
(3, ' = ', 1, ' plus', 2)
(6, ' = ', 3, ' plus', 3)
(10, ' = ', 6, ' plus', 4)
(15, ' = ', 10, ' plus', 5)
(21, ' = ', 15, ' plus', 6)
(28, ' = ', 21, ' plus', 7)
([28, 21, 15, 10, 6, 3, 1], ' updated row')
"""
      
