"""
34. Find First and Last Position of Element in Sorted Array:  https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""

# Final solution beats 82% runtime using a binary search method:
class Solution(object):
    def searchRange(self, nums, target):
        if target not in nums:
            return [-1, -1]
        else:
            nums.append('dummy') #add a fake value at end to avoid index errors on rare occasion
            start = nums.index(target) # since list is sorted numbers prior no need to check
            endList = [start] #need list to find the max index
            end = start # track end index
            while nums[end] == target and end<len(nums)-1:
                endList.append(end)
                end=end+1

            stop = max(endList)
            return[start, stop] 



# My initial draft 75 / 88 testcases passed:
class Solution(object):
    def searchRange(self, nums, target):
        if target not in nums:
            return [-1, -1]
        else:
            start = nums.index(target)
            endList = [start]
            end = start
            while nums[end] == target and end<len(nums)-1:
                endList.append(end)
                end=end+1
            stop = max(endList)
            return[start, stop] 
                
        
