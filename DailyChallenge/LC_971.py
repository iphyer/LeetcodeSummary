# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        self.res = []
        self.index = 0
        self.FLAG = True
        
        def preOrder(node):
            if not node: return
            if node.val != voyage[self.index]:
                self.FLAG = False
                return
            self.index += 1
            if self.index < len(voyage) and node.left and node.left.val != voyage[self.index]:
                # swap
                self.res.append(node.val)
                preOrder(node.right)
                preOrder(node.left)
            else:
                preOrder(node.left)
                preOrder(node.right)

        preOrder(root)
        if self.FLAG:
            return self.res
        else:
            return [-1]
