# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        out = []
        if not root:
            return out
        queue.append(root)

        while queue:
            size = len(queue)
            level = []
            for i in range(size):
                curr_root = queue.popleft()
                level.append(curr_root.val)
                if curr_root.left:
                    queue.append(curr_root.left)
                if curr_root.right:
                    queue.append(curr_root.right)
            out.append(level)
        return out