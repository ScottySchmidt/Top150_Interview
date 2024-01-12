"""
1004. Max Consecutive Ones III: https://leetcode.com/problems/max-consecutive-ones-iii/
Top 75 Interview Question! 

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
"""

# Sliding Window Accepted Solution:
class Solution(object):
    def longestOnes(self, nums, k):
        left = right = maxSize = 0 
        n = len(nums)
        # checks for edge cases: 
        while left < n and right < n:
            # while correct:
            if k != 0 or nums[right] == 1:
                if nums[right]==0:
                    k = k -1 # used a remain
                right = right+1
            # incorrect, out of count:
            elif k == 0:
                if nums[left] == 0:
                    k += 1
                left = left+1 
            curLen = right-left # get length
            maxSize = max(maxSize, curLen) # store new size
        return maxSize
