# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        if k == 1: return [head]
        n, curr = 0, head
        # get length of the linked list
        while curr:
            n += 1
            curr = curr.next
        # get each parts length
        # each k parts length = n // k
        #   first n%k parts add 1
        len_k, remaining_len_k = n//k, n%k

        # split linked list
        res = []
        curr, prev = head, head
        curr_part = 1

        while curr_part <= k:
            curr_head = curr
            curr_len = 1
            # adding len_k
            while curr_len <= len_k:
                prev = curr
                curr = curr.next
                curr_len += 1
            # if first n%k parts, adding additional one
            if curr_part <= remaining_len_k:
                prev = curr
                curr = curr.next
            # break next link if needed
            if prev:
                prev.next = None
                res.append(curr_head)
            else:
                res.append(None)
            curr_part += 1
        return res
