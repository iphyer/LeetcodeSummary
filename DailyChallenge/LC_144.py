# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        
        def DFS(node):
            if not node: return
            res.append(node.val)
            DFS(node.left)
            DFS(node.right)
        
        DFS(root)
        return res
            
