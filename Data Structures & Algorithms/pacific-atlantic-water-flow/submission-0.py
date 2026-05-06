class Solution:
    def check(self, row, col, heights, ocean):
        ocean[row][col] = True
        lst = [[row+1, col], [row-1, col], [row, col+1], [row, col-1]]

        for r, c in lst:
            if 0 <= r < len(heights) and 0 <= c < len(heights[0]) and not ocean[r][c] and heights[r][c] >= heights[row][col]:
                self.check(r, c, heights, ocean)

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        rows, cols = len(heights), len(heights[0])
        pac = [[False for i in range(cols)] for j in range(rows)]
        atl = [[False for i in range(cols)] for j in range(rows)]

        for i in range(rows):
            self.check(i, 0, heights, pac)
            self.check(i, cols-1, heights, atl)

        for i in range(cols):
            self.check(0, i, heights, pac)
            self.check(rows-1, i, heights, atl)

        for r in range(rows):
            for c in range(cols):
                if pac[r][c] and atl[r][c]:
                    res.append([r, c])

        return res