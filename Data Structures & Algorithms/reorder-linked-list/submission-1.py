# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = slow = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next


        head_2 = slow.next
        l1 = head
        slow.next = None

        # revert head_2:
        prev = None
        curr = head_2
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        l2 = prev

        while l2:
            nl1, nl2 = l1.next, l2.next
            l1.next = l2
            l2.next = nl1
            l1, l2 = nl1, nl2
        



