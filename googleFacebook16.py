"""
16. 3Sum Closest https://leetcode.com/problems/3sum-closest/description/

Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
------------------------------
"""

# Original solution passes 28 / 99 cases:
class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest = 9999

        for i in range(len(nums)-2):
            start = 0
            end = len(nums) - 1
            while start < end:
                s = nums[i] + nums[start] + nums[end]
                diff = abs(s - target)
                if diff < closest:
                    closest = diff
                if s < target:
                    start = start+1
                elif s > target:
                    end = end-1
                else: 
                    return s
        return closest
