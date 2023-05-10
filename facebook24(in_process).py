"""
24. Swap Nodes in Pairs: https://leetcode.com/problems/swap-nodes-in-pairs/description/

Given a linked list, swap every two adjacent nodes and return its head. 
You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]
"""

# Evenually I found this simple solution:
class Solution:
    def swapPairs(self, head):
        dummy = pre = ListNode(0)
        pre.next = head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, a.next, b.next = b, b.next, a
            pre = a
        return dummy.next

# Work in progress have detailed commments:
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        dummy = ListNode(0, head) # add a 0 at beg to avoid index error
        prev, curr = dummy, head
        #cur is ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: None}

        while curr and curr.next:  # This will be [1 and 2] and evenually [3 and 4]
            # SAVE POINTERS:
            nxtPair = curr.next.next # 3
            second = curr.next # 2

            # SWAP PAIRS:
            second.next = curr  # second.next is now 1 evenually 3
            curr.next = nxtPair  # curr.next is now 3  instead of 2 and 4
            prev.next = second # second is 2 then 4 # Head of dummy node must point to 2 as its beg of NodeList
            print(dummy)

            # SET POINTERS FOR NEXT LOOP:
            prev = curr # set to 1 with 3 as next
            curr = nxtPair # curr becomes 3 (which means curr.next is now 4) 
        return dummy.next # dummy without next would have a 0
        
