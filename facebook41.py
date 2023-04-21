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

# This solution runs into memory error, so how do we make this into O(n) time and uses constant extra space?
class Solution:
    def firstMissingPositive(self, nums):
        nums.sort()

        for i in range(1, len(nums)+2):
            if i not in nums:
                return i
