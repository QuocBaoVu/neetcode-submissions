class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = lo + (hi-lo)//2
            # checksort:
            if target == nums[mid]:
                return mid
            if nums[lo] <= nums[mid]:
                # this means left half is sorted
                if nums[lo] <= target and target < nums[mid]:
                    hi = mid-1 # fuck right side
                else:
                    lo = mid+1
            else:
                # this means right side is sorted:
                if target > nums[mid] and nums[hi] >= target:
                    lo = mid + 1 # fuck left side
                else:
                    hi = mid - 1
        return -1