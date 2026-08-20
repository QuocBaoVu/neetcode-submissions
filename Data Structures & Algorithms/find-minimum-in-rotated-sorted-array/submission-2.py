class Solution:
    def findMin(self, nums: List[int]) -> int:

        lo = 0
        hi = len(nums) - 1

        while lo < hi:
            mid = lo + (hi-lo)// 2
            # # checksort:
            # if target == nums[mid]:
            #     return mid
            if nums[hi] < nums[mid]:
                # this means left half is sorted, minimum is in right side:
                lo = mid + 1
            else:
                # this means right half is sorted, minimum can be from mid to left:
                hi = mid

        return nums[hi]
