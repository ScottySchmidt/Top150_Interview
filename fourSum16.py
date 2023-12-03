"""
18. 4Sum https://leetcode.com/problems/4sum/

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
"""

# Beats 50% runtime: 
class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        quads = set()
        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):
                start = j + 1
                end = n-1
                two = nums[i] + nums[j]
                while start < end:
                    total = nums[start] + nums[end] + two
                    if total < target:
                        start = start+1
                    elif total > target:
                        end = end -1
                    else:
                        quads.add((nums[i], nums[j], nums[start], nums[end]))     
                        end=end-1
                        start=start+1
        return quads
    
"""
In order to make this solution faster, some continue the sorted list on equal values to avoid duplicates.
But I find my solution easier to understand and more readable using a set.
"""
