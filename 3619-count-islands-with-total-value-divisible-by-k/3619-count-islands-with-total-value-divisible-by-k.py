class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def dfs(r,c):
            if (r not in range(rows) or c not in range(cols) or grid[r][c] == 0 or (r,c) in visit):
                return 0
            visit.add((r,c))

            total = grid[r][c]
            total += dfs(r-1,c)
            total += dfs(r+1,c)
            total += dfs(r,c-1)
            total += dfs(r,c+1)

            return total
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 0 and (r,c) not in visit:
                    total = dfs(r,c)
                    if total % k == 0:
                        islands += 1
        return islands
        