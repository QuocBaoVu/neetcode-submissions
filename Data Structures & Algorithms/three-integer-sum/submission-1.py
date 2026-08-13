class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        out = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0:
                break
            target = 0 - nums[i]
            left = i+1
            right = n-1
            while left < right:
                tot = nums[left] + nums[right]
                if tot == target:
                    out.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                    
                elif tot > target:
                    right -= 1
                else:
                    left += 1
        
        return out
