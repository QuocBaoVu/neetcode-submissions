class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        heap = []

        for i in nums:
            freq[i] += 1
        
        for i in freq.keys():
            heapq.heappush(heap, (freq[i], i))
            if len(heap) > k:
                heapq.heappop(heap)
        
        out = [i[1] for i in heap]
        return out