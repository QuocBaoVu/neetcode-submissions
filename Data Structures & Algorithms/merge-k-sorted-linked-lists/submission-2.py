# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:


        heap = []
        tie = 0

        for i, lst in enumerate(lists):
            curr = lst
            while curr:
                heapq.heappush(heap, (curr.val, tie, curr))
                tie += 1
                curr = curr.next
                out = ListNode()
        
        out = ListNode()
        curr = out

        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
        curr.next = None

        return out.next