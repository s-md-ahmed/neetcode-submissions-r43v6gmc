from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        Let’s dry-run this specific input step-by-step.

### The Input Board

```
Row 0: ["X", "X", "X", "X"]
Row 1: ["O", "O", "O", "X"]
Row 2: ["X", "X", "X", "X"]
Row 3: ["X", "X", "X", "X"]

```

---

### Step 1: The "Edge Sweep"

The code loops through every cell on the border and calls `capture(r, c)` if it finds an `'O'`.

1. **Starts scanning:**
* Row 0: No 'O's.
* **Row 1, Col 0:** Found an `'O'`! It's on the edge. Call **`capture(1, 0)`**.
* Row 2 & 3: No 'O's.


2. **Inside `capture(1, 0)`:**
* Mark `board[1][0] = 'T'`.
* Try neighbors:
* `capture(2, 0)` -> It's `'X'`, **return**.
* `capture(0, 0)` -> It's `'X'`, **return**.
* **`capture(1, 1)`** -> It's an `'O'`, so it calls `capture(1, 1)`.
* Mark `board[1][1] = 'T'`.
* Try neighbors:
* `capture(2, 1)` -> `'X'`, **return**.
* `capture(0, 1)` -> `'X'`, **return**.
* **`capture(1, 2)`** -> It's an `'O'`, so it calls `capture(1, 2)`.
* Mark `board[1][2] = 'T'`.
* Try neighbors:
* All directions (`2,2`, `0,2`, `1,3`, `1,1`) are `'X'` or `'T'`, so all **return**.




* `capture(1, 0)` -> It's `'T'` (already visited), **return**.




* `capture(1, -1)` -> Out of bounds, **return**.





**State of board after Step 1:**

```
["X", "X", "X", "X"],
["T", "T", "T", "X"],
["X", "X", "X", "X"],
["X", "X", "X", "X"]

```

---

### Step 2: The "Final Sweep"

Now the code loops through the entire board one last time to fix the values.

* `board[0][0..3]`: All `'X'`. (No change)
* `board[1][0]`: Is `'T'`. **Change back to `'O'**`.
* `board[1][1]`: Is `'T'`. **Change back to `'O'**`.
* `board[1][2]`: Is `'T'`. **Change back to `'O'**`.
* `board[1][3]`: Is `'X'`. (No change)
* `board[2][0..3]`: All `'X'`. (No change)
* `board[3][0..3]`: All `'X'`. (No change)

---

### Final Result

```
["X", "X", "X", "X"],
["O", "O", "O", "X"],
["X", "X", "X", "X"],
["X", "X", "X", "X"]

```

**Conclusion:** Since the `'O'`s were connected to the edge, the algorithm correctly identified them as survivors, marked them temporarily, and then restored them to their original state, leaving the rest of the `'X'`s alone.


        """
        if not board:
            return
        
        ROWS, COLS = len(board), len(board[0])

        def capture(r, c):
            # If we are out of bounds or not an 'O', stop
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != 'O':
                return
            
            # Mark as a "survivor" (Temporary marker)
            board[r][c] = 'T'
            
            # Explore neighbors
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        # 1. Start from the edges to find all 'O's connected to the border
        for r in range(ROWS):
            for c in range(COLS):
                if (r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1) and board[r][c] == 'O':
                    capture(r, c)

        # 2. Sweep the board to update everything
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    # If it's still 'O', it's surrounded (not connected to edge)
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    # Change our temporary markers back to 'O'
                    board[r][c] = 'O'