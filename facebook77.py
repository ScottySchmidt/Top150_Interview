"""
77. Combinations  https://leetcode.com/problems/combinations/description/
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
You may return the answer in any order.

Example 1:
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.

"""
# Beats 54% runtime using backtracking:
class Solution(object):
    def combine(self, n, k):
        result = []
        # Adding n+1 here outside function gives 15% beat runtime speed!
        end=n+1 # need to add one since using range later. 
        def backtrack(start, curList):
            if len(curList)==k: # found a combo
                result.append(curList[:]) # must be a copy since curList mutates 
                return # no longer need to check
            # always check between start and end
            for i in range(start, end):
                curList.append(i) # list now has new num
                # i+1 ensures a number is never added twice to curList
                backtrack(i+1, curList) 
                curList.pop() # once backtrack finishes, need to pop to continue 

        backtrack(1, []) # start at 1 since using range (not an index at 0)
        return result
