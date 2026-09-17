class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return []
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = collections.deque()


        def helper(r, c):
            if (r, c) in visited or min(r, c) < 0 or r == rows or c == cols or grid[r][c] == -1:
                return
            
            q.append([r, c])
            visited.add((r, c))
        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visited.add((r, c))
        

        distance = 0
        while q:
            n = len(q)
            for i in range(n):
                r, c = q.popleft()
                grid[r][c] = distance
                helper(r + 1, c)
                helper(r - 1, c)
                helper(r, c + 1)
                helper(r, c - 1)

            distance += 1

