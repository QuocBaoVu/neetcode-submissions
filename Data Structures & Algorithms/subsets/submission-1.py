class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []
        n = len(nums)
        def btr(path, start):
            out.append(path[:])

            for i in range(start, n):
                path.append(nums[i])
                btr(path, i+1)
                path.pop()
    
        btr([], 0)
        return out
            