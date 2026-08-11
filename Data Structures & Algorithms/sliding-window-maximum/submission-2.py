class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        n = len(nums)
        out = [0] * (n-k+1)
        heap = [] # (-value, index)

        for right in range(k):
            heapq.heappush(heap, (-nums[right], right))
        out[0] = -heap[0][0]

        for right in range(k, n):
            heapq.heappush(heap, (-nums[right], right))
            # range: right - k + 1 : right

            while heap[0][1] < right-k+1 or heap[0][1] > right:
                heapq.heappop(heap)
        
            out[right - k + 1] = -heap[0][0]
            left += 1
        return out