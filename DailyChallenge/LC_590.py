"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        """
        Iterative
        """
        if not root: return []
        queue = deque([root])
        res_queue = deque([])
        while queue:
            node = queue.popleft()
            for child in node.children:
                queue.appendleft(child)
            res_queue.appendleft(node.val)
        return res_queue
        
        """
        recursive
        """
        
        """
        if not root: return []
        res = []
        
        def DFS(node):
            for child in node.children:
                DFS(child)
            res.append(node.val)
            
        DFS(root)
        return res
        """
