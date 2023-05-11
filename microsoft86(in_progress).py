""" 
86. Partition List https://leetcode.com/problems/partition-list/description/

Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Example 2:

Input: head = [2,1], x = 2
Output: [1,2]

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""


# This method gets confusing due to having to return the original before_head.next
class Solution(object):
    def partition(self, head, x):
        before_head= before = ListNode(-1)
        after_head = after  = ListNode(-1)
        print(before)

        while head:
            if head.val < x:
                before.next = head
                before = before.next
                head = head.next
            else:
                after.next = head
                after = after.next
                head=head.next
        
        after.next = None  # after.next is nothing
        before.next = after_head.next # connect before to after (must be the original after_head)
        return before_head.next # merged list
