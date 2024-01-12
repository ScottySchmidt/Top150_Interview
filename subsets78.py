"""
78. Subsets https://leetcode.com/problems/subsets/description/

Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
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
