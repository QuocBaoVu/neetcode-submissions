class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x : x[0])
        output = 0 
        merged = []
        for interval in intervals:
            if not merged or interval[0] >= merged[-1][1]:
                # No-overlap:
                merged.append(interval)
            else:
                output += 1
                merged[-1][1] = min(merged[-1][1] , interval[1])
        return output