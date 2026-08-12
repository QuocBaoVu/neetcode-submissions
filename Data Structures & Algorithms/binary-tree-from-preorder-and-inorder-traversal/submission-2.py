# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hash_map = defaultdict(int)
        for i in range(len(inorder)):
            hash_map[inorder[i]] = i
        pre_i = 0
        def build(in_left, in_right):
            nonlocal pre_i
            if in_left > in_right:
                return None
            
            root_val = preorder[pre_i]
            pre_i += 1
            root = TreeNode(root_val)

            in_i = hash_map[root_val]

            root.left = build(in_left, in_i-1)
            root.right = build(in_i+1, in_right)

            return root

        return build(0, len(preorder)-1)
        # left: 0 -> idx-1
        # right idx + 1 -> n





