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

# Final solution:
class Solution:
    def threeSum(self, nums):
        ans = []
        nums.sort()

        for i in range(len(nums)-2):
            start = i+1
            end = len(nums)-1
            while start < end:  
                # Get Three Distinct Numbers:
                n = nums[i]
                l = nums[start]
                r = nums[end]
                s = n+l+r
                if s > 0:
                    end=end-1
                elif s < 0:
                    start=start+1
                else:
                    trio=[n, l, r]
                    if trio not in ans:
                        ans.append(trio)
                    start=start+1
                    end=end-1
        return ans




# My initial solution gets runtime error:
class Solution:
    def threeSum(self, nums):
        ans = []
        l = 0
        r = len(nums)-1
        nums.sort()

        while l+1 < r:  
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
                if trio not in ans:
                    ans.append(trio)
        return ans
