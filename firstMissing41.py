"""
 41. First Missing Positive: https://leetcode.com/problems/first-missing-positive/

Given an unsorted integer array nums, return the smallest missing positive integer.
You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Example 1:
Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.
"""

# Correct Solution, wrong runtime:
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
