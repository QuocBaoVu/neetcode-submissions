class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)

        if tot % 2 == 1:
            return False

        # Find a subset that sum is tot//2
        n = len(nums)
        target = tot//2
        dp = {}

        def dfs(i, target):
            if (i, target) in dp:
                return dp[(i, target)]
            if i == n:
                if target == 0:
                    dp[(i, target)] = True
                    return True
                else:
                    dp[(i, target)] = False
                    return False
            else:
                dp[(i, target)] = dfs(i+1, target) or dfs(i+1, target-nums[i])

            return dp[(i, target)]
        
        return dfs(0, target)