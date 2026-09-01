class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)

        dp[0] = 0

        for i in range(1, amount+1):
            out = float('inf')
            for c in coins:
                if i - c < 0:
                    continue
                out = min(out, dp[i-c] + 1)
            dp[i] = out
        
        return -1 if dp[amount] == float('inf') else dp[amount]