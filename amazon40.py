"""
40. Combination Sum II

Companies Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
"""

# 20 / 176 testcases passed
def combinationSum2(self, candidates, target):
    candidates.sort()
    ans=[]
    def new(cur, start, target):
        if target==0:     
            copy = cur[:] # [:] is same as list.copy() in python 3.8
            copy.sort()
            if copy not in ans:
                ans.append(copy)  
        if target <= 0:
            return
        n=len(candidates)
        for i in range(start, n):
            num = candidates[i]
            cur.append(num)
            new(cur, start+1, target-num)
            cur.pop()
    new([], 0, target)
    return ans 



# 124 / 176 testcases passed, runtime error:
class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        
        import itertools
        ans = []

        stuff = candidates
        for L in range(len(stuff) + 1):
            for subset in itertools.combinations(stuff, L):
                if sum(subset) == target and subset not in ans:
                    ans.append(subset)
        return ans
