class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        visited = set()
        rows, cols = len(grid), len(grid[0])
        def dfs(r, c):
            if (r < 0 or r == rows or c < 0 or c == cols or grid[r][c] == 2 or grid[r][c] == 0):
                return 0
            
            grid[r][c] = 2

            return 1 + dfs(r + 1, c) + dfs(r, c + 1) + dfs(r - 1, c) + dfs(r , c - 1)


        area = 0
        for i in range(rows):
            for j in range(cols):
                area = max(area, dfs(i, j))
        
        return area