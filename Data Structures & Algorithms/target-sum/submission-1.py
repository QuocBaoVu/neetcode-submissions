class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # dp[i][j]: number of way we can reach i: i-> -sum to sum of nums using first j element in nums

        n = len(nums)

        # recursion: 
        # dp[i][j] = dp[i - nums[j-1]][j-1] + dp[i + nums[j-1]][j-1]
        memo = defaultdict(int)
        memo[0] = 1

        for i in range(n):
            new_memo = defaultdict(int)
            for tot in memo:
                new_add = tot + nums[i]
                new_sub = tot - nums[i]

                new_memo[new_add] += memo[tot]
                new_memo[new_sub] += memo[tot]

            memo = new_memo

        return memo[target]
        # def solve(tot, i):
        #     if (tot, i) in memo:
        #         return memo[(tot,i)]
        #     if i == n:
        #         out = 0
        #         if tot == target:
        #             out = 1
        #         memo[(tot, i)] = out
        #         return out
        #     val = nums[i]
        #     memo[(tot, i)] = solve(tot+val, i+1) + solve(tot-val, i+1)
        #     return memo[(tot,i)]

        solve(0,0)
        return memo[(0, 0)]