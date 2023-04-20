"""
Apple Hard 42. Trapping Rain Water  https://leetcode.com/problems/trapping-rain-water/description/

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped.
"""

# My current solution passes 318/322 solutions, but uses too much memory for complicated arrays:
class Solution(object):
    def trap(self, height):
        r=len(height)

        rightsMax=[]
        
        for i in range(0, r):
            rights=height[i:r]
            rMax=max(rights)
            rightsMax.append(rMax)

        #first left is always 0
        leftsMax=[0]
        for x in range(1, r):
            lefts=height[0:x]
            lMax=max(lefts)
            leftsMax.append(lMax)

        finalList=[]
        for i in range(0, r):
            low=min(rightsMax[i], leftsMax[i])
            water=low-height[i]
            finalList.append(water)
        
        #print(rightsMax, " rights")
        #print(leftsMax, " lefts")
        finalList = [0 if i < 0 else i for i in finalList]
        #print(finalList, " final")
        return sum(finalList)
