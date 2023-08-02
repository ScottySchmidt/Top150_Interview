"""
11. Container With Most Water:  https://leetcode.com/problems/container-with-most-water/

You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.
"""
    
# Linear runtime final solution using two pointers::
class Solution(object):
    def maxArea(self, height):
        max_area = 0 
        l = 0 
        r = len(height) - 1

        while l < r:  
            h = min(height[l], height[r])
            w = r-l

            area = h * w
            max_area = max(area, max_area)
            if height[l] <= height[r]:
                l=l+1
            else:
                r=r-1
        return max_area


# Brute force gets runtime error:
class Solution(object):
    def maxArea(self, height):
        length = len(height)
        max_area = 0 

        for l in range(0, length):
            for r in range(l+1, length):
                small = min(height[l], height[r])
                diff = r-l

                area = small * diff
                max_area = max(area, max_area)
        return max_area
  
