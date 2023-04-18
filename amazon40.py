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
