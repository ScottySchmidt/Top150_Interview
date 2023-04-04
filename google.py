"""
4. Median of Two Sorted Arrays: https://leetcode.com/problems/median-of-two-sorted-arrays/description/
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
This problem is considered HARD because of coding efficiency. 
My solution is good, but considered slow in comparision to chatGBT.
"""

# My solution with 39% runtime and 28% memory:
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

        
        
# ChatGBT solution that beats 92% runtime and 80% memory:        
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        # ensure nums1 is shorter
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        # lengths of both arrays
        m, n = len(nums1), len(nums2)
        
        # binary search on nums1
        left, right, half_len = 0, m, (m + n + 1) // 2
        while left <= right:
            i = (left + right) // 2
            j = half_len - i
            
            if i < m and nums2[j-1] > nums1[i]:
                # i is too small, increase it
                left = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                # i is too big, decrease it
                right = i - 1
            else:
                # i is perfect
                
                # find maximum element on the left partition
                if i == 0:
                    max_left = nums2[j-1]
                elif j == 0:
                    max_left = nums1[i-1]
                else:
                    max_left = max(nums1[i-1], nums2[j-1])
                    
                # if the total length of the arrays is odd
                if (m + n) % 2 == 1:
                    return max_left
                
                # find minimum element on the right partition
                if i == m:
                    min_right = nums2[j]
                elif j == n:
                    min_right = nums1[i]
                else:
                    min_right = min(nums1[i], nums2[j])
                    
                # if the total length of the arrays is even
                return (max_left + min_right) / 2.0
