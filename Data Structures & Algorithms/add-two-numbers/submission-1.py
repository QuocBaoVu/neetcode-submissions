# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        remain = 0
        head_l1 = l1
        head_l2 = l2

        while l1.next and l2.next:
            l1=l1.next
            l2=l2.next
        while l1.next:
            l1=l1.next
            l2.next=ListNode(0)
            l2=l2.next
        while l2.next:
            l2=l2.next
            l1.next=ListNode(0)
            l1=l1.next

        l1 = head_l1
        l2 = head_l2

        while l1 and l2:
            tot = l1.val + l2.val
            if remain:
                tot += 1
            if tot > 9:
                val = tot-10
                remain = 1
            else:
                val = tot
                remain = 0
            curr.next = ListNode(val)
            curr = curr.next
            l1=l1.next
            l2=l2.next
        
        if remain:
            curr.next = ListNode(1)
        return dummy.next
            
        