"""
80. Remove Duplicates from Sorted Array II: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. 
The relative order of the elements should be kept the same.
Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. 
It does not matter what you leave beyond the first k elements.
Return k after placing the final result in the first k slots of nums.
Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Custom Judge:
The judge will test your solution with the following code:
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.


Example 1:
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""
# Clean two pointers accepted solution, need to reattempt this problem. 
# Also, this problem checks index 1 to 3 and not 1, 2, and 3? Need to consider how this is accepted.
class Solution(object):
    def removeDuplicates(self, nums):
      if len(nums) < 2:
          return nums # Cannot have a triple dup with two nums
          
      pointer = 1 
      for i in range(2, len(nums)):
          if nums[pointer-1] != nums[i]:  
               pointer+=1
               nums[pointer] = nums[i] 
          # else: If one is equal to three nums and pointer does not update
      return pointer+1 # add 1since index started at 0 not 1
""" This solution starts at changing index 3 first without changing first two index.
This looks confusing at first, but when you think about it the first two index will never need to be chnaged
since it cannot be a triple dup.
""
    
