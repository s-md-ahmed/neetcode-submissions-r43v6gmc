class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjlist = {i: [] for i in range(numCourses)}
        in_degree = [0] * numCourses
        
        for dest, src in prerequisites:
            adjlist[src].append(dest)
            in_degree[dest] += 1
            
        queue = [i for i in range(numCourses) if in_degree[i] == 0]
        
        result = []
        finished = 0
        while queue:
            curr = queue.pop(0)
            result.append(curr)
            finished += 1
            
            for neighbor in adjlist[curr]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # If finished count matches numCourses, we have a valid order
        return result if finished == numCourses else []