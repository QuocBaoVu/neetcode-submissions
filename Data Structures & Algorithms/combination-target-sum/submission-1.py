class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        out = []
        n = len(nums)
        nums.sort()

        def backtrack(start, path, target):
            if target == 0:
                out.append(path[:])
                return
            for i in range(start, n):
                if nums[i] > target:
                    break
                path.append(nums[i])
                backtrack(i, path, target-nums[i])
                path.pop()
        
        backtrack(0, [], target)
        return out