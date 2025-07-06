# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodes_in_A = set()
        current = headA
        
        # Store all nodes of List A in a set
        while current:
            nodes_in_A.add(current)  # or `nodes_in_A.add(id(current))`
            current = current.next
        
        # Check if any node in List B exists in the set
        current = headB
        while current:
            if current in nodes_in_A:  # or `if id(current) in nodes_in_A`
                return current
            current = current.next
        
        return None  # No intersection