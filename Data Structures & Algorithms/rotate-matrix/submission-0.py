class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Transpose: swap matrix[i][j] with matrix[j][i]
        matrix[:] = [list(row) for row in zip(*matrix)]
        for row in matrix:
            row.reverse()
        