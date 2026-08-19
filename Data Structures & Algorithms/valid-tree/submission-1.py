class UFDS:
    def __init__(self, n:int):
        self.parent = [i for i in range(n)]
        self.weight = [0] * n
        self.counter = n
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def unite(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return False
        if self.weight[px] < self.weight[py]:
            px, py = py, px
        self.parent[py] = px
        if self.weight[px] == self.weight[py]:
            self.weight[px] += 1
        self.counter -= 1
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        ufds = UFDS(n)

        for e in edges:
            u, v = e
            if not ufds.unite(u,v):
                return False
        if ufds.counter == 1:
            return True
        return False