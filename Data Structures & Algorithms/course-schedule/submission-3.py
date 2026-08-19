class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        queue = deque()

        in_degree = [0] * numCourses
        nbrs = defaultdict(list)

        for p in prerequisites:
            u, v = p
            in_degree[v] += 1
            nbrs[u].append(v)

        for u in range(numCourses):
            if in_degree[u] == 0:
                queue.append(u)

        while queue:
            curr = queue.popleft()
            for nbr in nbrs[curr]:
                in_degree[nbr] -= 1
                if in_degree[nbr] == 0:
                    queue.append(nbr)
            
        for u in range(numCourses):
            if in_degree[u] != 0:
                return False
        return True