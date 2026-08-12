# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def traverse(root, bound):
            out = 0
            if not root:
                return 0
            
            if root.val >= bound:
                out = 1
            new_bound = max(bound, root.val)

            return out + traverse(root.left, new_bound) + traverse(root.right, new_bound)
        
        return traverse(root, -101)

