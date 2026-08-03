# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # head_pointer = [ListNode() for _ in lists]

        # for i in range(len(lists)):
        #     head_pointer[i] = lists[i]

        heap = []

        for lst in lists:
            curr = lst
            while curr:
                heapq.heappush(heap, curr.val)
                curr = curr.next
        
        out = ListNode()

        curr = out

        while heap:
            val = heapq.heappop(heap)
            curr.next = ListNode(val)
            curr = curr.next

        return out.next