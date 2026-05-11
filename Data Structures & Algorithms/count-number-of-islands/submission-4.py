class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        numIslands = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    numIslands += 1
                    queue = deque([(r, c)])
                    grid[r][c] = "0"

                    while queue:
                        row, col = queue.popleft()

                        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            newR, newC = row + dr, col + dc

                            if (0 <= newR < rows and 0 <= newC < cols and grid[newR][newC] == "1"):
                                queue.append((newR, newC))
                                grid[newR][newC] = "0"
        
        return numIslands