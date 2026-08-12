class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = [[]]
        n = len(nums)
        def btr(start, arr):
            if start >= n:
                return
            for i in range(start, n):
                arr.append(nums[i])
                out.append(arr[:])
                btr(i+1, arr)
                arr.pop()
    
        btr(0, [])
        return out
            