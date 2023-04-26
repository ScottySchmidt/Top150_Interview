"""
Apple Hard 42. Trapping Rain Water  https://leetcode.com/problems/trapping-rain-water/description/

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped.
"""

# Final Solution using two points left and right:
class Solution:
    def trap(self, height):
        n = len(height)
        if n < 3:
            return 0
        water = 0
        left = 1 
        right = n-2
        left_max = height[0]
        right_max = height[n-1]

        while left <= right:
            if left_max < right_max:
                left_max = max(left_max, height[left]) 
                amount=left_max-height[left]
                if amount > 0:
                    water += amount
                left=left+1 
            else:
                right_max = max(right_max, height[right])
                amount = right_max-height[right]
                if amount > 0:
                    water += amount
                right=right-1
        return water


# Fast runtime but only 122 / 322 testcases passed
class Solution(object):
    def trap(self, height):
        n=len(height)

        maxLeftList=[]
        maxRightList=[]

        curRightMax = -1
        curLeftMax = -1
        for l in range(n):
            maxR=max(height[l], curRightMax)
            curRightMax=maxR
            maxRightList.append(maxR)

        for r in range(n-1, -1, -1):
            leftR = max(height[r], curLeftMax)
            curLeftMax = leftR
            maxLeftList.append(leftR)

        #print(maxLeftList)
        #print(maxRightList)
        total = 0
        for i in range(1, n-1): #first and last is always 0
            less=min(maxLeftList[i], maxRightList[i])
            water=less-height[i]
            
            if water>0:
                total=total+water
        return total

# My current solution passes 318/322 solutions, but uses too much memory for complicated arrays:
class Solution(object):
    def trap(self, height):
        n=len(height)

        maxLeftList=[]
        maxRightList=[]
        for l in range(n):
            maxR=max(height[l:n])
            maxRightList.append(maxR)

        for r in range(1, n+1):
            leftR = max(height[0:r])
            maxLeftList.append(leftR)

        total = 0
        for i in range(n):
            less=min(maxLeftList[i], maxRightList[i])
            water=less-height[i]
            if water>0:
                total=total+water
        return total

