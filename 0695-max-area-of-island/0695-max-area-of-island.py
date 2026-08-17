class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        max_count = 0

        def dfs(r,c):
            if (r not in range(rows) or c not in range(cols) or (r,c) in visited or grid[r][c] != 1):
                return 0 
            visited.add((r,c))
            count = 1
            count += dfs(r-1,c)
            count += dfs(r+1,c)
            count += dfs(r,c-1)
            count += dfs(r,c+1)
            return count
            

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    size = dfs(r,c)
                    visited.add((r,c))
                    max_count = max(max_count, size)
        
        return max_count


