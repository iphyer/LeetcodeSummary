# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        node = head
        N = 0
        while node:
            N += 1
            if N == k: p1 = node
            node = node.next
        n2 = N-k+1
        curr = 0
        node = head
        while node:
            curr += 1
            if curr == n2: 
                p2 = node
                break
            node = node.next
        p1.val, p2.val = p2.val, p1.val
        return head

 # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        p1 = None
        p2 = None
        curr = head
        
        while curr:
            k -= 1
            if p2: p2 = p2.next
            if k == 0:
                p1 = curr
                p2 = head
            curr = curr.next
        # swap two nodes
        p1.val, p2.val = p2.val, p1.val
        return head
