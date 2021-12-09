"""

post-order DFS

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        def totalSum(node):
            if not node: return 0
            
            left_sum = totalSum(node.left)
            right_sum = totalSum(node.right)
            tilt = abs(right_sum - left_sum)
            self.ans += tilt
            
            return left_sum + right_sum + node.val
        totalSum(root)
        return self.ans
