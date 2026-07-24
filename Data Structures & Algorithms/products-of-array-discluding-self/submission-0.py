class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * (n+1)
        right = [1] * (n+1)
        out = [1] * n
        
        for i in range(n):
            left[i+1] = left[i] * nums[i]
        
        for i in range(n-1, -1, -1):
            right[i] = right[i+1] * nums[i]

        for i in range(n):
            out[i] = left[i] * right[i+1]
        return out


        # [-1,0,1,2,3] -> [0, -6 .]
        # left: [1, -1, 0, 0 , 0, 0 ] right: [0,0,6,6,3,1]