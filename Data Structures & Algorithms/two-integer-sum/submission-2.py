class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        
        for i in range(len(nums)):
            n = nums[i]
            if target - n in table:
                return [table[target-n], i]
            table[nums[i]] = i
