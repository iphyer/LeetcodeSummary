# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast = head, head
        tot = 0
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # check odd or even
        if not fast: # even
            mid = slow
        else: # odd
            mid = slow.next
            
        # reverse starting from mid
        mid = self.reveserLL(mid)
        
        # compare palindromeLL
        p1 = head
        p2 = mid
        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True
        
    def reveserLL(self, head: ListNode) -> ListNode:
        newNext = None
        curr = head
        while curr:
            prev = curr.next
            curr.next = newNext
            newNext = curr
            curr = prev
        return newNext
