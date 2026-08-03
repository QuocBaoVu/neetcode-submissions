# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        heap = []
        p1 = list1
        p2 = list2

        while p1:
            heapq.heappush(heap, p1.val)
            p1 = p1.next
        
        while p2:
            heapq.heappush(heap, p2.val)
            p2 = p2.next
        
        out = ListNode()
        curr = out

        while heap:
            val = heapq.heappop(heap)
            curr.next = ListNode(val)
            curr = curr.next
        
        return out.next