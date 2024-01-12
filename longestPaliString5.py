"""
Given a string s, return the longest palindromic substring in s.
Medium: https://leetcode.com/problems/longest-palindromic-substring/description/

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
"""

class Solution(object):
    def longestPalindrome(self, s):
        res = ""
        resLen = 0

        for i in range(len(s)):
            # Odd Numbers:
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l+1 # new max 
                l = l-1  # Left one
                r = r+1  # Right one

            # Even Numbers:
            l, r = i, i + 1 # plus one will make this even only
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l+1
                l = l-1
                r = r+1
        return res
