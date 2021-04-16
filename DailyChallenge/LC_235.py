# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def getPath(node, target):
            path = []
            while node.val != target.val:
                path.append(node)
                if node.val > target.val:
                    node = node.left
                else:
                    node = node.right
            path.append(node)
            return path
        p_path = getPath(root, p)
        q_path = getPath(root, q)

        for i in range(len(p_path)-1, -1, -1):
            if p_path[i] in q_path:
                return p_path[i]

# second solution

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if ( p.val > root.val and q.val > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        if ( p.val < root.val and q.val < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        return root
