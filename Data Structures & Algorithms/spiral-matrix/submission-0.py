class Solution:
    '''
    To dry run the `[[1,2],[3,4]]` matrix, we follow the "shrinking boundaries" logic:

### Initial State

* `matrix`: `[[1, 2], [3, 4]]`
* `top = 0`, `bottom = 1`
* `left = 0`, `right = 1`
* `res = []`

---

### Step-by-Step Execution

**1. Traverse Right (Top row)**

* Loop from `left` (0) to `right` (1):
* Add `matrix[0][0]` (1)
* Add `matrix[0][1]` (2)


* `res = [1, 2]`
* `top` becomes **1**

**2. Traverse Down (Right column)**

* Loop from `top` (1) to `bottom` (1):
* Add `matrix[1][1]` (4)


* `res = [1, 2, 4]`
* `right` becomes **0**

**3. Traverse Left (Bottom row)**

* *Check:* `top (1) <= bottom (1)` is true.
* Loop from `right` (0) to `left` (0):
* Add `matrix[1][0]` (3)


* `res = [1, 2, 4, 3]`
* `bottom` becomes **0**

**4. Traverse Up (Left column)**

* *Check:* `left (0) <= right (0)` is **false** (since `right` became 0 in step 2).
* The loop skips.

### Final Result

* `res = [1, 2, 4, 3]`

The "walls" have effectively collapsed into the center, and you have visited every element exactly once. Does seeing the pointers change value-by-value make the logic feel more manageable?
    '''
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            # 1. Traverse Right
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            
            # 2. Traverse Down
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            
            if top <= bottom:
                # 3. Traverse Left
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1
                
            if left <= right:
                # 4. Traverse Up
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1
                
        return res