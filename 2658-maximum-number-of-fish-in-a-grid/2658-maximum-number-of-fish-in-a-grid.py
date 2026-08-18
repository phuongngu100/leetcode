class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fish = 0
        visit = set()

        def dfs(r,c):
            if (r not in range(rows) or c not in range(cols) or (r,c) in visit or grid[r][c] == 0):
                return 0
            visit.add((r,c))

            max_fish = grid[r][c]
            max_fish += dfs(r+1,c)
            max_fish += dfs(r-1,c)
            max_fish += dfs(r,c+1)
            max_fish += dfs(r,c-1)

            return max_fish
        
        for r in range(rows):
            for c in range(cols):
                num_fish = dfs(r,c)
                fish = max(fish,num_fish)
        return fish




        