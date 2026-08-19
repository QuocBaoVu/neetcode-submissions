class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        out = []
        in_degree = [0] * numCourses
        nbrs = defaultdict(list)
        queue = deque()

        for p in prerequisites:
            a, b = p
            in_degree[a] += 1
            nbrs[b].append(a)

        for u in range(numCourses):
            if in_degree[u] == 0:
                queue.append(u)

        while queue:
            curr = queue.popleft()
            out.append(curr)
            for nbr in nbrs[curr]:
                in_degree[nbr] -= 1
                if in_degree[nbr] == 0:
                    queue.append(nbr)

        for u in range(numCourses):
            if in_degree[u] != 0:
                return []
        
        return out