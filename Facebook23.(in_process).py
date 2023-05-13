"""
23. Merge k Sorted List, Hard LeetCode: https://leetcode.com/problems/merge-k-sorted-lists/
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
------------------------------------
"""

# Work In Progress:
class Solution(object):
    def mergeKLists(self, lists):
        v=[] 
        for i in lists:
            x=i # temp list
            print(x)
            while x:  # keep getting next item in list
                v+=[x.val] # add val to list
                x=x.next # next item
        v=sorted(v,reverse=True) # backwards list for now
        print(v, " v")
        ans=None
        for i in v:
            ans=ListNode(i,ans) # create a NodeList that will now be normal
        return ans
