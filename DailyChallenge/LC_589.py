"""

Recursive

"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        self.res = []
        
        def preOrder(node):
            if not node: return
            self.res.append(node.val)
            for n in node.children:
                preOrder(n)
        
        preOrder(root)
        return self.res

"""

Iterative

"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return []
        queue = deque([root])
        res = []
        
        while queue:
            node = queue.popleft()
            res.append(node.val)
            for child in reversed(node.children):
                queue.appendleft(child)
        return res
