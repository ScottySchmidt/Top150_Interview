"""
53. Maximum Subarray

Given an integer array nums, find the  subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxTotal = nums[0] # store best number
        curSum = 0 # potential new best
        for num in nums: # loop through every num
            if curSum < 0:
                curSum = 0 # need to find starting point
            curSum=curSum+num
            maxTotal=max(maxTotal, curSum)
        return maxTotal 
