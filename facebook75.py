"""
75. Sort Colors: https://leetcode.com/problems/sort-colors/description/

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.
"""
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count={0:0, 1:0, 2:0}

        # get the count of each num
        for n in nums:
            count[n] +=1
            #print(n, " add to ", counts)

        idx = 0
        for v in range(3):
            for c in range(count[v]):
                nums[idx] = v # v, starting at 0, will get put into 'c' (count) number of times
                idx+=1 # next index
        return
