class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # brute force:
        n = len(nums)
        dp = [1] * n
        for i in range(n-1, -1, -1):
            curr = nums[i]
            #i = 5
            for j in range(i, n):
                # j = 6
                if curr < nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
                


