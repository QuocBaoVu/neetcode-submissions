class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # column level:
        lo = 0
        hi = len(matrix)-1
        while lo < hi:
            mid = (lo +hi +1) // 2
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] > target:
                hi = mid-1
            if matrix[mid][0] < target:
                lo = mid
        
        row = matrix[lo]

        lo = 0
        hi = len(row) - 1

        while lo <= hi:
            mid = lo + (hi-lo) // 2
            if row[mid] == target:
                return True
            if row[mid] > target:
                hi = mid-1
            if row[mid] < target:
                lo = mid+1
        
        return False