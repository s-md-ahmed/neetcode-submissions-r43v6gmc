'''
Setup State
adjlist = {0: [], 1: [0]}

in_degree = [1, 0]

queue = [1]

The while Loop (Surgical Precision)
Iteration 1:

curr = queue.pop(0) -> curr is now 1.

if curr in adjlist:

Since 1 is a key in our adjlist (it is 1: [0]), the condition is True.

for neighbor in adjlist[curr]:

We look at adjlist[1], which is [0]. So neighbor is 0.

in_degree[0] becomes 0.

Since in_degree[0] == 0, we queue.append(0).

finished becomes 1.

Iteration 2:

curr = queue.pop(0) -> curr is now 0.

if curr in adjlist:

We check if 0 is in adjlist. It is a key (it is 0: []).

The condition if curr in adjlist is True.

for neighbor in adjlist[curr]:

We look at adjlist[0]. It is an empty list [].

The for loop has nothing to iterate over. It does not run.

finished becomes 2.

case when u get false
Setup State
adjlist = {0: [], 1: [0]}

in_degree = [1, 0]

queue = [1]

The while Loop (Surgical Precision)
Iteration 1:

curr = queue.pop(0) -> curr is now 1.

if curr in adjlist:

Since 1 is a key in our adjlist (it is 1: [0]), the condition is True.

for neighbor in adjlist[curr]:

We look at adjlist[1], which is [0]. So neighbor is 0.

in_degree[0] becomes 0.

Since in_degree[0] == 0, we queue.append(0).

finished becomes 1.

Iteration 2:

curr = queue.pop(0) -> curr is now 0.

if curr in adjlist:

We check if 0 is in adjlist. It is a key (it is 0: []).

The condition if curr in adjlist is True.

for neighbor in adjlist[curr]:

We look at adjlist[0]. It is an empty list [].

The for loop has nothing to iterate over. It does not run.

finished becomes 2.
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = {i: [] for i in range(numCourses)}
        print(adjlist)
        for dest, src in prerequisites:
            adjlist[src].append(dest) 
        print(adjlist)
        
        in_degree = [0] * numCourses


        for dest, src in prerequisites:
            in_degree[dest] += 1
        print(in_degree)
        queue=[]
        for course in range(numCourses):
            if in_degree[course] == 0:
                queue.append(course)
        finished=0
        while queue:
            curr=queue.pop(0)
            if curr in adjlist:
                for neighbor in adjlist[curr]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)
            finished+=1


        return finished==numCourses