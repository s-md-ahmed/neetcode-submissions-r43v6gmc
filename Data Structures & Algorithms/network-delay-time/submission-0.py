"""
DRY RUN:
Input: times = [[1,2,1],[2,3,1],[1,4,4],[3,4,1]], n = 4, k = 1

1. Initialize: graph = {1: [(2,1), (4,4)], 2: [(3,1)], 3: [(4,1)]}, 
   pq = [(0,1)], dist = {}

2. Pop (0,1) where time=0, u=1: 
   - dist = {1: 0}
   - Push neighbors of 1 (v=2, w=1 and v=4, w=4): (1,2), (4,4) -> pq = [(1,2), (4,4)]

3. Pop (1,2) where time=1, u=2:
   - dist = {1: 0, 2: 1}
   - Push neighbors of 2 (v=3, w=1): (2,3) [1+1] -> pq = [(2,3), (4,4)]

4. Pop (2,3) where time=2, u=3:
   - dist = {1: 0, 2: 1, 3: 2}
   - Push neighbors of 3 (v=4, w=1): (3,4) [2+1] -> pq = [(3,4), (4,4)]

5. Pop (3,4) where time=3, u=4:
   - dist = {1: 0, 2: 1, 3: 2, 4: 3}
   - pq = [(4,4)]

6. Pop (4,4) where time=4, u=4:
   - Node 4 is already in dist (dist[4]=3), skip.

Result: max(0, 1, 2, 3) = 3
"""

import heapq
import collections

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        # Build adjacency list: u=source, v=destination, w=weight/time
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        # Priority Queue: (time, u)
        pq = [(0, k)]
        # Store shortest time to reach each node u
        dist = {}
        
        while pq:
            # time = accumulated time, u = current node
            time, u = heapq.heappop(pq)
            
            # If we have already visited node u, skip
            if u in dist:
                continue
            dist[u] = time
            
            # Check all neighbors v of current node u with edge weight w
            for v, w in graph[u]:
                if v not in dist:
                    heapq.heappush(pq, (time + w, v))
                    
        # If all n nodes are in dist, return max time; otherwise -1
        return max(dist.values()) if len(dist) == n else -1