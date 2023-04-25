"""
18. 4Sum: https://leetcode.com/problems/4sum/description/ 
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
"""

class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        quads = set()
        n = len(nums)

        for i in range(n-1):
            for j in range(i+1, n):  # i+1 so does not double add same number
                start = j + 1  # j+1 so does not double add same number
                end = n-1
                two = nums[i] + nums[j]
                while start < end:
                    total = nums[start] + nums[end] + two  
                    # Need a bigger number:
                    if total < target: 
                        start = start+1  
                    # Need a smaller number:
                    elif total > target:
                        end = end -1
                    # Found a quad:
                    else:
                        quads.add((nums[i], nums[j], nums[start], nums[end]))  # add quad to unique set
                        
                        # need new star and end num:
                        end=end-1
                        start=start+1
        return quads
