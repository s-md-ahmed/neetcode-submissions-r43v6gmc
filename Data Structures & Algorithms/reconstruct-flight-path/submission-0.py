import collections
'''
To do a "full detail" dry run, we have to track three things at every step: the **`graph`** (what flights remain), the **`path`** (the airports added when we get stuck), and the **`current location`**.

### Setup

**Input:** `tickets = [["HOU","JFK"],["SEA","JFK"],["JFK","SEA"],["JFK","HOU"]]`

**1. Build the sorted graph:**

* `JFK`: `["HOU", "SEA"]`
* `HOU`: `["JFK"]`
* `SEA`: `["JFK"]`

---

### Dry Run (DFS Traversal)

| Step | Current Airport | Action | Graph Status | Path (Result list) |
| --- | --- | --- | --- | --- |
| **Start** | JFK | Start DFS | `JFK:[HOU, SEA], HOU:[JFK], SEA:[JFK]` | `[]` |
| **1** | JFK | Fly to **HOU** (pops HOU) | `JFK:[SEA], HOU:[JFK], SEA:[JFK]` | `[]` |
| **2** | HOU | Fly to **JFK** (pops JFK) | `JFK:[SEA], HOU:[], SEA:[JFK]` | `[]` |
| **3** | JFK | Fly to **SEA** (pops SEA) | `JFK:[], HOU:[], SEA:[JFK]` | `[]` |
| **4** | SEA | Fly to **JFK** (pops JFK) | `JFK:[], HOU:[], SEA:[]` | `[]` |
| **5** | JFK | **Stuck** (no flights) | `JFK:[], HOU:[], SEA:[]` | `["JFK"]` |
| **6** | Backtrack to SEA | **Stuck** | `JFK:[], HOU:[], SEA:[]` | `["JFK", "SEA"]` |
| **7** | Backtrack to JFK | **Stuck** | `JFK:[], HOU:[], SEA:[]` | `["JFK", "SEA", "JFK"]` |
| **8** | Backtrack to HOU | **Stuck** | `JFK:[], HOU:[], SEA:[]` | `["JFK", "SEA", "JFK", "HOU"]` |
| **9** | Backtrack to JFK | **Stuck** | `JFK:[], HOU:[], SEA:[]` | `["JFK", "SEA", "JFK", "HOU", "JFK"]` |

---

### Final Result

The `path` list is now `["JFK", "SEA", "JFK", "HOU", "JFK"]`.
We perform `path[::-1]` to reverse it, giving us: **`["JFK", "HOU", "JFK", "SEA", "JFK"]`**.

### Summary of the "Stuck" Logic

* You only add an airport to the `path` list when you have **zero** outgoing flights left from that airport.
* Because you start at `JFK` and end at `JFK`, the `JFK` you got stuck at is indeed the absolute final destination, which is why it sits at the very end of your `path` list.
* Reversing it puts the starting `JFK` back where it belongs: at the front.

Does seeing the `path` list grow step-by-step make the "stuck and reverse" logic perfectly clear now?
'''
class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        # Build the graph
        graph = collections.defaultdict(list)
        # Sort tickets to ensure we pick lexicographically smallest first
        # We sort them by destination, then build the adjacency list
        for u, v in sorted(tickets, key=lambda x: x[1]):
            graph[u].append(v)
        print(graph)
        
        path = []
        
        def dfs(u):
            # While there are outgoing flights from u
            while graph[u]:
                # Pop the lexicographically smallest neighbor
                v = graph[u].pop(0)
                dfs(v)
            # Add to path after visiting all neighbors (post-order)
            path.append(u)
            
        dfs("JFK")
        # Reverse because we added nodes as we backtracked
        return path[::-1]