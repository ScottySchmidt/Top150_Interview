"""
46. Permutations: https://leetcode.com/problems/permutations/description/

Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""

# Beats 93% using iterrools: https://stackoverflow.com/questions/104420/how-do-i-generate-all-permutations-of-a-list
import itertools

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return list(itertools.permutations(nums))
