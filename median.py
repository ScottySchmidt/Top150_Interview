"""
4. Median of Two Sorted Arrays: https://leetcode.com/problems/median-of-two-sorted-arrays/description/
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Not sure how this problem is cosnidered "Hard" level. 
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        a = nums1 + nums2
        a.sort()
        l = len(a)
        mid = l // 2
        if l % 2 != 0:  # if odd
            return a[mid]/1 # // takes the floor num
        else:  # if even
            return (a[mid]+a[mid-1])/2.0 #2.0 will return as a float
