"""
47. Permutations II: https://leetcode.com/problems/permutations-ii/ 

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
"""

class Solution(object):
    def permuteUnique(self, nums):
        res = [] # final answer
        perm = []

        # find the count of each number:
        count = {n:0 for n in nums}
        for n in nums:
            count[n] += 1
        def search():
            if len(perm) == len(nums):  # if curlist equals lenth of nums, then a perm is found:
                if perm[:] not in res:
                    res.append(perm[:]) # must store a copy 
                return # not longer check
            
            for n in count:
                if count[n] > 0:
                    perm.append(n)
                    count[n] -= 1
                    
                    search() 

                    count[n] += 1
                    perm.pop()       
        search()
        return res
