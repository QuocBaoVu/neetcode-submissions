class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)
        if total % 2 == 1:
            return False

        target = total // 2

        #knapsack
        dp = [False] * (target+1)
        dp[0] = True
        # dp[i] = dp[i - n] or dp[i]
        for n in nums:
            for i in range(target, n-1, -1):
                dp[i] = dp[i] or dp[i-n] 

        return dp[target]


            
