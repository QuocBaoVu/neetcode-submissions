class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest_seen = float('inf')
        out = 0

        for price in prices:
            out = max(out, price - smallest_seen)
            smallest_seen = min(smallest_seen, price)
        return out