"""
209. Minimum Size Subarray Sum:  https://leetcode.com/problems/minimum-size-subarray-sum/

Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1
Input: target = 7, nums = [2,3,1,2,4,3]

Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
"""
# Final Accepted Solution using sliding window with start/end pointers:
class Solution(object):
    def minSubArrayLen(self, target, nums):
        n = len(nums)
        total = 0
        start = 0
        minSubArr = 987654321 # need a higher original number
        for end in range(n):
            total += nums[end]
            while total >= target:
                length = end-start+1 # length of subarr
                minSubArr = min(minSubArr, length) # store new min         
                # Nums Start is now plus one index:
                total -= nums[start] 
                start +=1
        # if minSubArr has not changed, then nothing was found:
        if minSubArr==987654321:
            return 0
        else:
            return minSubArr


# Passes 7/20 test cases:
class Solution(object):
    def minSubArrayLen(self, target, nums):
        n = len(nums)
        total = 0
        start = 0
        minSubArr = 9999
        
        for end in range(n):
            total += nums[end]
            if total >= target:
                length = end-start+1 # length of subarr
                minSubArr = min(minSubArr, length) # store new min
                start +=1
        if minSubArr==9999:
            return 0
        else:
            return minSubArr
