class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def rob_simple(nums):
            # dp[i] = nums[i] + max(dp[i-2], dp[i-3]) 
            if not nums:
                return 0
            n = len(nums)
            if n == 1:
                return nums[0]
            if n == 2:
                return max(nums)
            dp = [0] * n
            dp[0] = nums[0]
            dp[1] = nums[1]
            dp[2] = nums[0]+nums[2]

            for i in range(3, n):
                dp[i] = nums[i] + max(dp[i-2], dp[i-3])
            
            return max(dp)
        if len(nums) == 1:
            return nums[0]
        take_one = rob_simple(nums[:-1])
        take_two = rob_simple(nums[1:])
        return max(take_one, take_two)
