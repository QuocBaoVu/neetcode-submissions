class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)

        # dp[(i,j)] could you reach target=j when using first i nums
        dp[0] = 1
        n = len(nums)
        for i in range(n):
            new_dp = defaultdict(int)
            for tot in dp:
                new_add = tot + nums[i]
                new_sub = tot - nums[i]
                new_dp[new_add] += dp[tot] 
                new_dp[new_sub] += dp[tot] 
            dp = new_dp

        return dp[target]