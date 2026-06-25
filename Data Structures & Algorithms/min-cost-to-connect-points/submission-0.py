import heapq
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        # min_heap stores tuples of (cost, point_index)
        min_heap = [(0, 0)]
        visited = [False] * n
        total_cost = 0
        edges_count = 0
        
        while edges_count < n:
            cost, i = heapq.heappop(min_heap)
            
            # If the point is already connected, skip it
            if visited[i]:
                continue
                
            # Add the point to the MST
            visited[i] = True
            total_cost += cost
            edges_count += 1
            
            # Calculate distance to all other non-visited points
            for next_i in range(n):
                if not visited[next_i]:
                    dist = abs(points[i][0] - points[next_i][0]) + \
                           abs(points[i][1] - points[next_i][1])
                    heapq.heappush(min_heap, (dist, next_i))
                    
        return total_cost