class Solution(object):
    def numEnclaves(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            if grid[r][c] == 0:
                return

            grid[r][c] = 0

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Remove all land connected to boundary
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)

        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)

        # Count remaining land
        count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    count += 1

        return count
        