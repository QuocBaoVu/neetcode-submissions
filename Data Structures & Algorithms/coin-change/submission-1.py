class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # State: dp[i] the min number of coin used to create i amount of money
        # dp[i] = min(dp[i-k]) + 1
        
        # dp = [0] * (amount+1)
        # # Base case:
        # dp[0] = 0
        

        dp = [-1] * (amount+1)
        if not dp:
            return 0
        dp[0] = 0


        for i in range(1, amount+1):
            best = float('inf')
            for c in coins:
                if i - c < 0 or dp[i-c] == -1:
                    continue
                best=min(best, dp[i-c]+1)
            dp[i] = best

        return dp[amount] if dp[amount] != float('inf') else -1



        