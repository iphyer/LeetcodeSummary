# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0
        self.res = 0
        def DFS(node, pathMax):
            if node.val >= pathMax: 
                self.res += 1
                pathMax = node.val
            if node.left: DFS(node.left, pathMax)
            if node.right: DFS(node.right, pathMax)
        
        DFS(root, root.val)
        return self.res
