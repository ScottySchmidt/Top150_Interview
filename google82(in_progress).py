"""
82. Remove Duplicates from Sorted List II: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. 
Return the linked list sorted as well.

Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
"""

#  Wrote detailed comments how to solve this problem. Attempting a solution from memory soon:
class Solution(object):
    def deleteDuplicates(self, head):
        dummy = ListNode(0, head) # add a 0 to dummy node 
        cur = head # curr node
        prev = dummy # prev node since has 0 at beg
        while cur and cur.next:  # check two cur nodes at a time
            if cur.val == cur.next.val: 
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next # keep "skipping cur"
                # SET NEXT LOOP:
                cur = cur.next  # time to check next num
                prev.next = cur # Previous pointer now points to cur since nodes got deleted
            else:
                # SET NEXT LOOP:
                prev = cur # store prev num
                cur=cur.next # 1 becomes next 2
        return dummy.next # next is needed to not return the original 0 dummy node
