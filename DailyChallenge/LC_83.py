# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = prev = curr = ListNode(-101, head)
        curr = curr.next
        while curr:
            while curr and prev.val == curr.val:
                curr = curr.next
            if prev.next != curr:
                # duplicate
                prev.next = curr
            prev = curr
            if curr: curr = curr.next
        return dummy.next
