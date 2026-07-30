class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        def find(total, rest):
            if total == 0:
                return True
            if not rest:
                return False
            result = False
            for i in rest:
                remain = rest[:]
                remain.remove(i)
                result = result or find(total-i, remain)
            return result
        
        total = sum(nums)
        if total % 2 == 1:
            return False

        return find(total/2, nums)
        


            
