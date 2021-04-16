# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        newNext = None
        curr = head
        while curr:
            prev = curr.next
            curr.next = newNext
            newNext = curr
            curr = prev
        return newNext
