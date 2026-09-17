class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        time = 0
        q = collections.deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while fresh > 0 and q:
            n = len(q)
            for i in range(n):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1):
                       grid[nr][nc] = 2
                       q.append((nr, nc))
                       fresh -= 1

            time += 1

        return time if fresh == 0 else -1

                
            