class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        idx = 0
        n = len(intervals)
        result = []
        while idx < n and intervals[idx][1] < newInterval[0]:
            result.append(intervals[idx])
            idx += 1
        
        while idx < n and intervals[idx][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0],intervals[idx][0])
            newInterval[1] = max(newInterval[1],intervals[idx][1])
            idx += 1
        result.append(newInterval)
        
        while idx < n:
            result.append(intervals[idx])
            idx += 1



        return result
 