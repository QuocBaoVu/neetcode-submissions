class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        def merge(t1, t2):
            ai, bi, ci = t1
            aj, bj, cj = t2
            return [max(ai, aj), max(bi, bj), max(ci, cj)]

        inf = -float('inf')
        triplet = [inf, inf, inf] 

        for t in triplets:
            for i in range(3):
                # if can find a triplet, containing a value in target, record the best
                if t[i] == target[i]:
                    merged = merge(t, triplet)
                    if merged == target:
                        return True
                    if merged[0] <= target[0] and merged[1] <= target[1] and merged[2] <= target[2]:
                        triplet = merged
        return False
        # After this, combine 3 triplets to check
