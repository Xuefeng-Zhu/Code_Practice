# Given a linked list, determine if it has a cycle in it.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        a = head
        b = head
        while b is not None and b.next is not None:
            a = a.next
            b = b.next.next
            if a == b:
                return True
        return False
        