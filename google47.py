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

# To beter understand see output comments at very end:
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
                res.append(perm[:]) # must store a copy 
                print(perm[:], " found")
                return # not longer check
            
            for n in count:
                if count[n] > 0:
                    perm.append(n)
                    print(n, " added")
                    count[n] -= 1
                    
                    search() 

                    count[n] += 1
                    print(perm, " about to pop")
                    perm.pop()
                    print("pop ", perm)       
        search()
        return res
       
"""
(1, ' added')
(1, ' added')
(2, ' added')
([1, 1, 2], ' found')
([1, 1, 2], ' about to pop')
('pop ', [1, 1])
([1, 1], ' about to pop')
('pop ', [1])
(2, ' added')
(1, ' added')
([1, 2, 1], ' found')
([1, 2, 1], ' about to pop')
('pop ', [1, 2])
([1, 2], ' about to pop')
('pop ', [1])
([1], ' about to pop')
('pop ', [])
(2, ' added')
(1, ' added')
(1, ' added')
([2, 1, 1], ' found')
([2, 1, 1], ' about to pop')
('pop ', [2, 1])
([2, 1], ' about to pop')
('pop ', [2])
([2], ' about to pop')
('pop ', [])
"""
