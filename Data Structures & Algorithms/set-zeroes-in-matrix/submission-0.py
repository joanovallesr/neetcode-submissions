class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        firstRowZero = False
        firstColZero = False

        for c in range(n):
            if matrix[0][c] == 0:
                firstRowZero = True
                break
        
        for r in range(m):
            if matrix[r][0] == 0:
                firstColZero = True

        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        if firstRowZero:
            for c in range(n):
                matrix[0][c] = 0

        if firstColZero:
            for r in range(m):
                matrix[r][0] = 0