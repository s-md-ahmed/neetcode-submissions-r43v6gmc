from collections import defaultdict
'''
I hear you. You want to see the "math blackboard." Let's stop the abstract talk and lay out the exact variables for `count([3, 3])` on the blackboard.

### The Blackboard: `count([3, 3])`

* **Your Query Point (`px, py`):** `(3, 3)`
* **Your Data Structure (`self.pts`):** `[(1, 1), (2, 2), (1, 2)]`

Here is what the code is doing line-by-line in the loop:

| Iteration | `x, y` (from list) | `px, py` | Condition Check `abs(px-x) != abs(py-y)` | Status |
| --- | --- | --- | --- | --- |
| **1** | `(1, 1)` | `(3, 3)` | `abs(3-1) != abs(3-1)` $\rightarrow$ `2 != 2` (False) | **PASS** |
| **2** | `(2, 2)` | `(3, 3)` | `abs(3-2) != abs(3-2)` $\rightarrow$ `1 != 1` (False) | **PASS** |
| **3** | `(1, 2)` | `(3, 3)` | `abs(3-1) != abs(3-2)` $\rightarrow$ `2 != 1` (True) | **SKIP** |

---

### The Verification (Why it returns 0)

Now, let's look at the **PASS** iterations and see why they still result in `0`.

#### Iteration 1: `(1, 1)` is the candidate

* We found a valid diagonal! The other corners **must** be at `(px, y)` and `(x, py)`.
* Corner A: `(3, 1)`
* Corner B: `(1, 3)`
* **Code check:** `pts_count[(3, 1)] * pts_count[(1, 3)]`
* **Reality:** Your dictionary has no points at `(3, 1)` or `(1, 3)`. Both return `0`.
* **Math:** `0 * 0 = 0`.

#### Iteration 2: `(2, 2)` is the candidate

* We found a valid diagonal! The other corners **must** be at `(px, y)` and `(x, py)`.
* Corner A: `(3, 2)`
* Corner B: `(2, 3)`
* **Code check:** `pts_count[(3, 2)] * pts_count[(2, 3)]`
* **Reality:** Your dictionary has no points at `(3, 2)` or `(2, 3)`. Both return `0`.
* **Math:** `0 * 0 = 0`.

### The "Blackboard" Summary

The variables `px` and `py` **never change**. They are `3` and `3` for the entire duration of the `count([3, 3])` call. The loop only changes `x` and `y` by picking them one-by-one from `self.pts`.

You aren't checking if `(3, 3)` is "inside" the square; you are checking if `(3, 3)` can act as a **corner** for a square that uses one of your existing points as the **opposite diagonal**. Because your existing points don't have the "partner" corners needed to complete those squares, the math defaults to `0`.

Does looking at the `px, py` constants vs. the `x, y` loop variables make it click?
I hear you. You want to see the "math blackboard." Let's stop the abstract talk and lay out the exact variables for `count([3, 3])` on the blackboard.

### The Blackboard: `count([3, 3])`

* **Your Query Point (`px, py`):** `(3, 3)`
* **Your Data Structure (`self.pts`):** `[(1, 1), (2, 2), (1, 2)]`

Here is what the code is doing line-by-line in the loop:

| Iteration | `x, y` (from list) | `px, py` | Condition Check `abs(px-x) != abs(py-y)` | Status |
| --- | --- | --- | --- | --- |
| **1** | `(1, 1)` | `(3, 3)` | `abs(3-1) != abs(3-1)` $\rightarrow$ `2 != 2` (False) | **PASS** |
| **2** | `(2, 2)` | `(3, 3)` | `abs(3-2) != abs(3-2)` $\rightarrow$ `1 != 1` (False) | **PASS** |
| **3** | `(1, 2)` | `(3, 3)` | `abs(3-1) != abs(3-2)` $\rightarrow$ `2 != 1` (True) | **SKIP** |

---

### The Verification (Why it returns 0)

Now, let's look at the **PASS** iterations and see why they still result in `0`.

#### Iteration 1: `(1, 1)` is the candidate

* We found a valid diagonal! The other corners **must** be at `(px, y)` and `(x, py)`.
* Corner A: `(3, 1)`
* Corner B: `(1, 3)`
* **Code check:** `pts_count[(3, 1)] * pts_count[(1, 3)]`
* **Reality:** Your dictionary has no points at `(3, 1)` or `(1, 3)`. Both return `0`.
* **Math:** `0 * 0 = 0`.

#### Iteration 2: `(2, 2)` is the candidate

* We found a valid diagonal! The other corners **must** be at `(px, y)` and `(x, py)`.
* Corner A: `(3, 2)`
* Corner B: `(2, 3)`
* **Code check:** `pts_count[(3, 2)] * pts_count[(2, 3)]`
* **Reality:** Your dictionary has no points at `(3, 2)` or `(2, 3)`. Both return `0`.
* **Math:** `0 * 0 = 0`.

### The "Blackboard" Summary

The variables `px` and `py` **never change**. They are `3` and `3` for the entire duration of the `count([3, 3])` call. The loop only changes `x` and `y` by picking them one-by-one from `self.pts`.

You aren't checking if `(3, 3)` is "inside" the square; you are checking if `(3, 3)` can act as a **corner** for a square that uses one of your existing points as the **opposite diagonal**. Because your existing points don't have the "partner" corners needed to complete those squares, the math defaults to `0`.

Does looking at the `px, py` constants vs. the `x, y` loop variables make it click?
'''
class CountSquares:
    def __init__(self):
        
        self.pts_count = defaultdict(int)
        
        self.pts = []

    def add(self, point: list[int]) -> None:
        self.pts_count[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point: list[int]) -> int:
        px, py = point
        count = 0
        
        for x, y in self.pts:
            
            if abs(px - x) != abs(py - y) or px == x or py == y:
                continue
            
            
            count += self.pts_count[(px, y)] * self.pts_count[(x, py)]
            
        return count