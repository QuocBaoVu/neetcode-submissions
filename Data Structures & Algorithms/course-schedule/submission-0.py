class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Two checks to approved: not cycle, and visit all nodes

        # First, i create adj list
        adj_list = defaultdict(list)
        in_degree = [0] * numCourses

        for pair in prerequisites:
            adj_list[pair[0]].append(pair[1])
            in_degree[pair[1]] += 1
        
        queue = deque()

        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        
        visited_count = 0

        while queue:
            node = queue.popleft()
            visited_count += 1

            for nbr in adj_list[node]:
                in_degree[nbr] -= 1
                if in_degree[nbr] == 0:
                    queue.append(nbr)

        return visited_count == numCourses


        
        




