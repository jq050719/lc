class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # After rotation:
        # matrix transposed (swap rows and columns), then reverse all rows

        n = len(matrix)  # matrix is n x n

        # swap rows and columns
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # reverse all rows
        for i in range(n):
            matrix[i].reverse()
        
