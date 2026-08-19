class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = defaultdict(list)

        for f in flights:
            fr, to, pr = f
            adj_list[fr].append((pr,to))

        pq = [(0, src, 0)] #dist, node, hop
        best_hop = {}

        while pq:
            price, node, hop = heapq.heappop(pq)
            if node == dst:
                return price
            if hop > k:
                continue
            if node not in best_hop or best_hop[node] > hop:
                best_hop[node] = hop
                for nbr in adj_list[node]:
                    d_price, n_node = nbr
                    heapq.heappush(pq, (d_price + price, n_node, hop+1))

        return -1
