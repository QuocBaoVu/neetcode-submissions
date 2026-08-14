class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow=fast=0
        slow = nums[slow]
        fast = nums[nums[fast]]

        while slow!=fast:
            # slow = 2
            # fast = 2
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        fast = slow
        slow = 0

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow