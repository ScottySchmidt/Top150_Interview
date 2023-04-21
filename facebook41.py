"""
Facebook HARD 41. First Missing Positive: https://leetcode.com/problems/first-missing-positive/

Companies
Given an unsorted integer array nums, return the smallest missing positive integer.
You must implement an algorithm that runs in O(n) time and uses constant extra space.

Example 1:
Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
"""

# Solution Beats 62% but not in log(0) consant time after some thinking:
class Solution:
    def firstMissingPositive(self, nums):
        nums.sort()
        nums = set(nums)

        for i in range(1, len(nums)+2):
            if i not in nums:
                return 1
