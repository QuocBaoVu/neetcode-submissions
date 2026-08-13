# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        out = ListNode(next=head)
        slow = fast = out

        for i in range(n+1):
            fast=fast.next
        while fast:
            fast=fast.next
            slow=slow.next
        remove_node = slow.next
        slow.next = remove_node.next

        return out.next