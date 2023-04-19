"""
19. Remove Nth Node From End of List: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []

This problem looks easier than it is and more datastructure practice is needed!
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        # Find size of linkedList:
        size = 0
        temp = head
        while temp:
            temp=temp.next
            size=size+1
        
        # In the event we have to remove first:
        if n==size:
            return head.next
        
        # Loop through and skip "Nth" end of list
        temp = head
        num = size-n-1  # 5 - 2 -1 
        for i in range(num):
            temp=temp.next
        temp.next=temp.next.next # "Skips" the nth node in list
        return head #return the linkedList
