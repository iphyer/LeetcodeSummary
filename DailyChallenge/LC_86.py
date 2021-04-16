# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy1 = p1 = ListNode(0)
        dummy2 = p2 = ListNode(0)
        
        while head:
            if head.val < x:
                p1.next = head
                p1 = p1.next
            else:
                p2.next = head
                p2 = p2.next
            head = head.next
        # stop LinkedList
        p2.next = None
        # link two parts
        p1.next = dummy2.next
        return dummy1.next
