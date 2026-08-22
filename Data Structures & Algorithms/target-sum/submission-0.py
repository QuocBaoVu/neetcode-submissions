class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # dp[i][j]: number of way we can reach i: i-> -sum to sum of nums using first j element in nums

        n = len(nums)
        # s = sum(nums)
        # dp = [[0] * s for _ in range(n)]

        # recursion: 
        # dp[i][j] = dp[i - nums[j-1]][j-1] + dp[i + nums[j-1]][j-1]
        out = 0
        memo = defaultdict(int)
        def solve(tot, i):
            if (tot, i) in memo:
                return memo[(tot,i)]
            if i == n:
                out = 0
                if tot == target:
                    out = 1
                memo[(tot, i)] = out
                return out
            val = nums[i]
            memo[(tot, i)] = solve(tot+val, i+1) + solve(tot-val, i+1)
            return memo[(tot,i)]

        solve(0,0)
        return memo[(0, 0)]