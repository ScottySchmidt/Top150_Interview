"""
23. Merge k Sorted List, Hard LeetCode: https://leetcode.com/problems/merge-k-sorted-lists/
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []

# Definition for singly-linked list.
# class ListNode(object):f
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""

# Accepted Solution with 85% runtime beat, Work In Progress (will try to replicate again in near future):
class Solution(object):
    def mergeKLists(self, lists):
        v=[] 
        for lst in lists:
            cur=lst # temp list
            # print(cur)
            while cur:  # keep getting next item in list
                v+=[cur.val] # add val to list as a seperate num. Without brackets v would become a total sum.
                cur=cur.next # next item
        v=sorted(v,reverse=True) # backwards list for now
        # print(v, " v")
        ans=None
        for i in v:
            ans=ListNode(i,ans) # i is value with next node ans
        return ans # return as new linkedList Node
 
