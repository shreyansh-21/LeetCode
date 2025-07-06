# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        def getListLength(head):
            """Helper function to compute the length of a linked list."""
            length = 0
            while head:
                length += 1
                head = head.next
            return length

        lenA = getListLength(headA)
        lenB = getListLength(headB)

        # Adjust the longer list's head to align with the shorter one
        while lenA > lenB:
            headA = headA.next
            lenA -= 1

        while lenB > lenA:
            headB = headB.next
            lenB -= 1

        # Traverse both lists in sync until intersection or end
        while headA != headB:
            headA = headA.next
            headB = headB.next

        return headA  # Returns None if no intersection