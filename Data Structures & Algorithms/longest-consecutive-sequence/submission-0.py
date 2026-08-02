class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        out = 0
        for i in nums:
            if i-1 not in nset:
                curr = i
                n = 1
                while curr + 1 in nset:
                    n += 1
                    curr += 1
                out = max(out, n)
        return out