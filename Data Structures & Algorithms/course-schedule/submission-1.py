class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create graph
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        for p in prerequisites:
            u = p[0]
            v = p[1]
            graph[u].append(v)
            in_degree[v] += 1
        
        queue = deque()
        visited = 0
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
                visited += 1
        
        while queue:
            curr = queue.popleft()
            for nbr in graph[curr]:
                if in_degree[nbr] > 0:
                    in_degree[nbr] -= 1
                if in_degree[nbr] == 0:
                    queue.append(nbr)
                    visited += 1
        
        if visited == numCourses:
            return True
        return False
        