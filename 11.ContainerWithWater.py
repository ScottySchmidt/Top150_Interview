"""
LeetCode 11. Container With Most Water 
You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_height = 0
        l = 0
        r = len(height) -1

        while l < r: 
            left = height[l]
            right = height[r]
            min_height = min(left, right)
            width = r - l
            area = width * min_height
            if area > max_height:
                max_height = area
            if left > right:
                r = r -1
            else:
                l = l +1
    return max_height
