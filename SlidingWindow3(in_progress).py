"""
3. Longest Substring Without Repeating Characters:  https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

# Passes 91 / 987 testcases passed
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        substring = ""
        max_count = 0
        for c in s:
            if c in substring:
                char_index = substring.index(c) #gets FIRST occurence string
                subtring = s[char_index+1:]
                print("new subtring ", substring)
            else:
                substring += c
                max_count = max(max_count, len(substring))
                print(substring, max_count)
        return max_count
