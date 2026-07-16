class Solution {
    public int minCostConnectPoints(int[][] points) {
        int n = points.length;
        boolean[] visited = new boolean[n];
        int out = 0;
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);

        pq.add(new int[]{0,0});

        while (pq.size() > 0) {
            int[] curr = pq.poll();
            int idx = curr[1];
            if (visited[idx]) {
                continue;
            }
            int[] point = points[curr[1]];
            int dist = curr[0];
            out += dist;
            visited[curr[1]] = true;
            for (int i = 0; i < n; i++) {
                if (visited[i]) {
                    continue;
                }
                int[] new_point = points[i];
                int new_dist = Math.abs(new_point[0] - point[0]) + Math.abs(new_point[1] - point[1]);
                pq.add(new int[]{new_dist, i});
            }
        }

        return out;
    }
}
