# 3263. Convert Doubly Linked List to Array I

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
"""
class Solution:
    def toArray(self, root: 'Optional[Node]') -> List[int]:
        node = root
        res = []        
        while node:
            res.append(node.val)
            node = node.next
        return res
        
