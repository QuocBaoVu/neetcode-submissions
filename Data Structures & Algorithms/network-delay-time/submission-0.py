class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj_list = defaultdict(list)
        # Create list:
        for time in times:
            u, v, t = time
            adj_list[u].append((t,v))
        
        # Dijsktra

        pq = [(0, k)]
        count = 0
        dist = [float('inf')] * (n+1)
        dist[k] = 0


        while pq:
            time, u = heapq.heappop(pq)
            if time > dist[u]:
                continue
            for nbr in adj_list[u]:
                dt, v = nbr
                if time + dt < dist[v]:
                    dist[v] = time+dt
                    heapq.heappush(pq, (dist[v], v))

        out = max(dist[1:])

        return out if out != float('inf') else -1