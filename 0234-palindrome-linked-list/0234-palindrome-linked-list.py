# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         fast = head
#         slow = head

#         while fast and fast.next:
#             fast = fast.next.next
#             slow =slow.next
        
#         # reverse wala 

#         prev = None
#         while slow:
#             temp = slow.next
#             slow.next =prev
#             prev =slow
#             slow=temp
        
#         left,right = head,prev
#         while right:
#             if left.val != right.val:
#                 return False
#             left = left.next
#             right = right.next
#             return True
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l = []
        curr = head
        while curr:
            l.append(curr.val)
            curr = curr.next
        return l == l[::-1]   
        