class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # dp[i] = max(dp)

        n = len(nums)

        best_max = best_min = nums[0]

        out = nums[0]

        for i in range(1, n):
            if nums[i] >= 0:
                best_max = max(nums[i], best_max * nums[i])
                best_min = min(nums[i], best_min * nums[i])
            else:
                bmx, bmn = best_min, best_max
                best_max = max(nums[i], bmx * nums[i])
                best_min = min(nums[i], bmn * nums[i])
            out = max(out, best_max)
        
        return out

