"""
19. Remove Nth Node From End of List: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
"""

# The challenging part is doing if not fast: which is needed if the ListNode size is 2
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        slow = head
        fast = head

        for _ in range(n):
            fast=fast.next # fast gets a Nth head start.
        if not fast: # This will solve if ListNode size is 2
            return head.next # In event there is no more fast since we did not use a dummy at beginning

        while fast.next:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next  # the n value gets deleted because it eseentially gets skipped
        return head # the ListNode has changed so we can return head. This is the most confusing part, in my opinion.
