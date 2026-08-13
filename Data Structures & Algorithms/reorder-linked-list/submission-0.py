# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        if not head:
            return
        if not head.next:
            return

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        second_half = slow.next
        slow.next = None

        # Separated the 2 hald
        
        # revese second half
        def reverse(head):
            prev = None
            curr = head

            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        second_half = reverse(second_half)
        


        first_half = head
        
        while second_half:
            first_next = first_half.next
            second_next = second_half.next
            first_half.next = second_half
            second_half.next = first_next
            first_half = first_next
            second_half = second_next
        
