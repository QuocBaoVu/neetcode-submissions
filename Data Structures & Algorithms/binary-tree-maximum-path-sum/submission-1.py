# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        out = -1001

        def postOrder(root):
            nonlocal out
            if not root:
                return 0
            left = max(0,postOrder(root.left))
            right = max(0, postOrder(root.right))
            out = max(out, root.val + left + right)

            return root.val + max(left, right)
        
        postOrder(root)

        return out
        