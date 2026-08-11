# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "null"
        return ",".join([str(root.val), self.serialize(root.left), self.serialize(root.right)])
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data_arr = data.split(",")
        p = 0

        def deser():
            nonlocal p
            if p >= len(data_arr):
                return
            data = data_arr[p]
            p += 1
            if data == "null":
                return None
            root = TreeNode(int(data))
            root.left = deser()
            root.right = deser()
            return root

        return deser()