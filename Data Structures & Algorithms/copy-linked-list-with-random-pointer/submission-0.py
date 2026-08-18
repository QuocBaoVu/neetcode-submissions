"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        table = {}
        table[None] = None
        curr = head

        while curr:
            new_node = Node(curr.val)
            table[curr] = new_node
            curr = curr.next
        
        curr = head
        while curr:
            nxt_node = table[curr.next]
            nxt_rdn = table[curr.random]
            this = table[curr]
            this.next = nxt_node
            this.random = nxt_rdn
            curr = curr.next
        
        return table[head]




