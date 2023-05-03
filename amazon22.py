"""
22. Generate Parentheses: https://leetcode.com/problems/generate-parentheses/description/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
"""'

# This is great stack practice, I am in the process of commenting fully how this problem works:
class Solution(object):
    #Using n = 3 as an example with comments for full understanding
    def generateParenthesis(self, n):
        if n <= 0:
            return []
        stack = []
        res = []

        def backtrack(open, close): 
            if open == close == n:
                s="".join(stack)
                print(s, " answer")
                res.append(s)
                return 

            if open < n:
                stack.append("(")
                backtrack(open+1, close) 
                '''
                backtrack will send ((( until n is 3
                then continue to close and make )))
                '''
                stack.pop()
                print(stack, " popped")
                
            if close < open:
                stack.append(")")
                backtrack(open, close+1)
                stack.pop()
                print(stack, " popped")
    
        backtrack(0, 0)
        return res

'''
('((()))', ' answer')
(['(', '(', '(', ')', ')'], ' popped')
(['(', '(', '(', ')'], ' popped')
(['(', '(', '('], ' popped')
(['(', '('], ' popped')
('(()())', ' answer')
(['(', '(', ')', '(', ')'], ' popped')
(['(', '(', ')', '('], ' popped')
(['(', '(', ')'], ' popped')
('(())()', ' answer')
(['(', '(', ')', ')', '('], ' popped')
(['(', '(', ')', ')'], ' popped')
(['(', '(', ')'], ' popped')
(['(', '('], ' popped')
(['('], ' popped')
('()(())', ' answer')
(['(', ')', '(', '(', ')'], ' popped')
(['(', ')', '(', '('], ' popped')
(['(', ')', '('], ' popped')
('()()()', ' answer')
(['(', ')', '(', ')', '('], ' popped')
(['(', ')', '(', ')'], ' popped')
(['(', ')', '('], ' popped')
(['(', ')'], ' popped')
(['('], ' popped')
([], ' popped')
'''
