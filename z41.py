"""
41. First Missing Positive: https://leetcode.com/problems/first-missing-positive/description/
Given an unsorted integer array nums, return the smallest missing positive integer.
You must implement an algorithm that runs in O(n) time and uses constant extra space.

This problem is rather simple not sure how it is rated HARD.
If you do not use a set you get a memory error. This will decrease the amount of numbers it searches.
'""

class Solution(object): 
    def firstMissingPositive(self, nums):
        s = set(nums) # 
        l = len(nums)

        for i in range(1, l+2):
            if i not in s:
                return i
