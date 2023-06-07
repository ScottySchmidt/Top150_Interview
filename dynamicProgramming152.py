"""
152. Maximum Product Subarray. https://leetcode.com/problems/maximum-product-subarray/   Medium Amazon Interview Questions

Given an integer array nums, find a subarray that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

# Accepted Final Solution.
# The trick is to track the current min and current max because on a negative number they swap.
class Solution(object):
    def maxProduct(self, nums):
        n=len(nums)
        if n==0:
            return 0
        if n==1:
            return nums[0]

        max_product = nums[0]
        min_product = nums[0]
        result = nums[0]
        for num in nums[1:]:
            # On a negative number, min becomes max and max becomes min
            if num < 0:
                max_product, min_product = min_product, max_product
            min_product = min(num, min_product * num)
            max_product = max(num, max_product * num)
            result = max(max_product, result)
        return result
