# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        if not head.next: return head
        
        dummay1 = head
        dummay2 = head.next
        head_even = head.next
        curr = head.next.next
        
        while curr:
            # connect odd
            dummay1.next = curr
            dummay1 = curr
            # coonect even
            if curr.next:
                dummay2.next = curr.next
                dummay2 = curr.next
                curr = dummay2.next
            else:
                # even not exist
                dummay2.next = None
                break
            
        # Connect odd to even
        dummay1.next = head_even
        return head
        
        
