# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if not head: return 0
        res = head.val
        curr = head.next
        
        while curr:
            res *= 2
            res += curr.val
            curr = curr.next
        return res
            
        
