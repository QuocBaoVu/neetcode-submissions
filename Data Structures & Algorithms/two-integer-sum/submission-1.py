class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i in range(len(nums)):
            table[nums[i]] = i

        
        for i in range(len(nums)):
            n = nums[i]
            if target - n in table and i != table[target-n]:
                return [i , table[target-n]]
