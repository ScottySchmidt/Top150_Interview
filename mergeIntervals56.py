"""
Microsoft56. Merge Intervals: https://leetcode.com/problems/merge-intervals/description/
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""

# Final Accepted Solution:
class Solution(object):
    def merge(self, intervals):
        n = len(intervals)
        if n == 1: 
            return intervals

        intervals = sorted(intervals)
        output = [intervals[0]] # start with first 

        for start, end in intervals[1:]: # check the next after first
            lastEnd = output[-1][1] # get last in num
            if start <= lastEnd: 
                output[-1][1] = max(lastEnd, end) # update prev interval bigger of two ends
            else:
                output.append([start, end])
        return output
    
     
# First draft passes 10% of testcases. 
class Solution(object):
    def merge(self, intervals):
        n = len(intervals)
        if n==1: return intervals

        intervals=sorted(intervals)
        mergeList=[]
        r = 1

        while r < n:
            l=r-1
            if intervals[l][1] >= intervals[r][0]:
                one=intervals[l][0]
                two=max(intervals[r][1], intervals[l][1])
                print("overlap: newList ", one, two)
                mergeList.append([one, two])
                r=r+2
            else:
                mergeList.append(intervals[l])
                mergeList.append(intervals[r])
                r=r+1
        return mergeList
