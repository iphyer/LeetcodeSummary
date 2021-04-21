"""

Recursive

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        def checkMirror(node1, node2):
            # both None
            if not node1 and not node2: return True
            # One Not None, One None
            if not node1 or not node2 : return False
            # both not None
            return node1.val == node2.val and checkMirror(node1.right, node2.left) and checkMirror(node1.left, node2.right)
        
        if not root: return True
        return checkMirror(root.left, root.right)
        

"""

Iterative

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        queue = deque([root.left, root.right])
        
        while queue:
            node1 = queue.popleft()
            node2 = queue.popleft()
            
            # Both None
            if not node1 and not node2: continue
            
            # One None, One not None
            if not node1 or not node2: return False
            
            # Both not None
            if node1.val != node2.val: return False
            # Mirror
            queue.append(node1.left)
            queue.append(node2.right)
            
            queue.append(node1.right)
            queue.append(node2.left)
            
        return True
        
