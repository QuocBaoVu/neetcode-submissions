class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        parent = [i for i in range(n)]

        def find(x):
            if parent[x] == x:
                return x
            else:
                return find(parent[x])
        
        def unite(x, y):
            px = find(x)
            py = find(y)

            if px != py:
                parent[py] = px

        for edge in edges:
            u = edge[0]
            v = edge[1]

            unite(u, v)
         
        count = 0
        for i in range(len(parent)):
            if parent[i] == i:
                count += 1


        return count
        