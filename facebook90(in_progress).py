"""
90. Subsets II https://leetcode.com/problems/subsets-ii/description/

Given an integer array nums that may contain duplicates, return all possible subsets(the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
"""



"""
Passes 3/20 Test Cases.
This solution appens back to the curList in a different index spot which throws off some test cases.
After some research, I overcomplicated this. Normally just append starting with small list to bigger list.
"""
class Solution(object):
    def subsetsWithDup(self, nums):
        ans=[[],nums]
        def backtrack(curList):
            n = len(curList)-1
            #print(n, curList)
            if n==0:
                return
            else:
                for i in range(0, n):
                    #print("inside for loop: ", n, curList)
                    num=curList[i]
                    curList.remove(num)
                    ans.append(curList[:])
                    backtrack(curList)
                    curList.append(num)
        backtrack(nums)
        return ans
     
        
