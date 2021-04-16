# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            node = TreeNode(v)
            node.left = root
            return node
        # d != 1
        queue = [root]
        for i in range(d-2):
            currLen = len(queue)
            while currLen > 0:
                node = queue.pop(0)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                currLen -= 1
        for node in queue:
            tmpleft = node.left
            tmpright = node.right
            node.left = TreeNode(v)
            node.right = TreeNode(v)
            node.left.left = tmpleft
            node.right.right = tmpright
        return root

            
