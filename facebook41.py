"""
Facebook HARD 41. First Missing Positive: https://leetcode.com/problems/first-missing-positive/

Given an unsorted integer array nums, return the smallest missing positive integer.
You must implement an algorithm that runs in O(n) time and uses constant extra space.

Example 1:
Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
"""

# Final Accepted Solution with 45% runtime:
class Solution:
    def firstMissingPositive(self, nums):
        nums.sort()

        i=1
        for n in nums:
            print(n, " in sett")
            if n < i:
                continue
            elif (n != i):
                return i
            else:
                i=i+1
                print(i, " new i")
        return i

# O(n) time complexity passes 171 / 175 testcases passed
# This solution struggling with lists such as [1, 1000] returns 1 not 2?
class Solution:
    def firstMissingPositive(self, nums):
        nums.sort()
        sett = set(nums)
        i=1
        for s in sett:
            # Ignore nums less than 1:
            if s < 1:
                pass
            else:
                print(s, " s")
                if s != i:
                    return i 
                i=i+1
                print(i, " new i")
        return i


# Solution Beats 62% but not in log(0) consant time after some thinking:
class Solution:
    def firstMissingPositive(self, nums):
        nums.sort()
        nums = set(nums)

        for i in range(1, len(nums)+2):
            if i not in nums:
                return 1
