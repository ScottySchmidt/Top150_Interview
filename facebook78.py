"""
78. Subsets: Facebook https://leetcode.com/problems/subsets/description/

Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.
"""

# Beats 89% runtime using backtrack:
class Solution(object):
    def subsets(self, nums):
        ans = [[]]
        end = len(nums)

        def search(curList, start):
            for i in range(start, end):
                num = nums[i]
                curList.append(num)
                #print(curList)
                ans.append(curList[:]) # must store a copy of curList 
                search(curList, i+1)
                curList.pop()
        search([], 0)
        return ans
