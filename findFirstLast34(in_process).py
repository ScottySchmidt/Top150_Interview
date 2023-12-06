"""
34. Find First and Last Position of Element in Sorted Array: 
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
"""

# My initial correct solution has slow runtime amd not O(log n) runtime complexity.. How can we make this faster?
class Solution(object):
    def searchRange(self, nums, target):
        indexList = []
        count=0
        for n in nums:
            if n == target:
                i = nums.index(n)
                indexList.append(i+count)
                count=count+1
                
        if len(indexList)==0:
            return [-1, -1]
        else:
            #print(indexList)
            min_num = min(indexList)
            max_num = max(indexList)
            return [min_num, max_num]
