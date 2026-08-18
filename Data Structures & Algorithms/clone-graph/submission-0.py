"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        table = {}
        stack = deque()
        stack.append(node)
        table[node] = Node(node.val)


        while stack:
            curr = stack.pop()
            nbrs = curr.neighbors
            for nbr in nbrs: 
                if nbr not in table:
                    table[nbr] = Node(nbr.val)
                    stack.append(nbr)
                table[curr].neighbors.append(table[nbr])
        
        return table[node]




