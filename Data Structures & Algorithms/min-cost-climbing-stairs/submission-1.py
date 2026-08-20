class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        prev1 = cost[1]
        prev2 = cost[0]

        for i in range(2, n):
            curr = min(prev1, prev2) + cost[i]
            prev2, prev1 = prev1, curr

        return min(prev1, prev2)