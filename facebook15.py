"""
15. 3Sum  https://leetcode.com/problems/3sum/
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
-------------------------------------

Using a triple for loop is not good here as that would be log of O(n3).
Therefore, my solution uses a while loop with index i.
"""

# My initial solution gets runtime error:
class Solution(object):
    def threeSum(self, nums):
        combos = []
        l = 0
        r = len(nums)-1

        while l+1 < r:  #minus two so no index error (since n3 does i+2)

            # Get Three Distinct Numbers:
            n1 = nums[l]
            n2 = nums[l+1]
            r1 = nums[r]

            if n1+n2+r1 > 0:
                r=r-1
            elif n1+n2+r1 < 0:
                l=l+1
            else:
                trio=[n1, n2, r1]
                combos.append(trio)
        return combos
