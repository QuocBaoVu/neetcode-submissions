# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        out = -1
        count = 0
        def inOrder(root):
            nonlocal out
            nonlocal count
            if not root:
                return 0

            inOrder(root.left)
            count += 1
            if count == k:
                out = root.val
                return
            inOrder(root.right)
             
        inOrder(root)
        return out
        