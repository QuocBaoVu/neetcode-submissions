class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort()
        n = len(nums)
        def backtrack(start, path):
            out.append(path[:])
            for i in range(start, n):
                if i > start:
                    if nums[i] == nums[i-1]:
                        # skip
                        continue
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()
        backtrack(0, [])
        return out
            
                

