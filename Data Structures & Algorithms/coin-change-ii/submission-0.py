class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        dp = [0] * (amount+1) # number of way to reach i

        dp[0] = 1 # always one way to reach 0 -> not choose anything

        # dp[i] = 
        
        for i in range(n):
            c = coins[i]
            for j in range(1, amount+1):
                if j >= c:
                    dp[j] += dp[j-c]
        
        return dp[amount]