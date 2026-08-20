class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)

        def can_finish(piles, k, h):
            hour = 0
            for p in piles:
                hour += math.ceil(p/k)
            return hour <= h


        while lo < hi:
            mid = lo + (hi-lo) // 2

            # check mid:
            if can_finish(piles, mid, h):
                hi = mid
            else:
                lo = mid + 1

        return lo