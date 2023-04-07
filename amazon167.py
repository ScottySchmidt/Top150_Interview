"""
167. Two Sum II - Input Array Is Sorted  https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
"""

# Final Solution:
class Solution(object):
    def twoSum(self, numbers, target):
        l = 0 
        r = len(numbers)-1

        while l < r:
            total = numbers[l] + numbers[r] 
            if total<target:
                l=l+1 
            elif total>target:
                r=r-1
            else:
                return [l+1, r+1]


# Passes all tests but runtime error:
class Solution(object):
    def twoSum(self, numbers, target):
        length = len(numbers)
        l = 0 
        r = 1

        while r < length:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] < target:
                r=r+1
            else:
                l=l+l
                if l == r:
                    r=r+1
        
        # In the rare case r gets bigger than length like this test case [5,25,75]:
        s=len(numbers)-1 # only need to check the final "r" value now
        
        for i in range(0, length):
            if numbers[i] + numbers[s] == target:
                return [i+1, s+1]
