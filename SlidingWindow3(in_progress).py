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

# Final Accepted Solution with 77% runtime using sliding windows with 2 pointers:
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        beg = 0
        end = 0
        max_len = 0
        for c in s:
            word = s[beg:end]
            if c in word:
                cur_len = end-beg
                beg = beg+word.index(c)+1
                max_len = max(max_len, cur_len)
            end += 1
        if max_len < end-beg: # This happens when there is for instance only one char in s
            return end-beg 
        else:
            return max_len


# Attempt 879 / 987 testcases passed
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        beg = 0
        end = 0
        max_len = 0
        for c in s:
            word = s[beg:end]
            if c in word:
                cur_len = end-beg
                beg = beg+word.index(c)+1
                max_len = max(max_len, cur_len)
            end += 1
        return max_len



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
