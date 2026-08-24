class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        length = 0

        def dfs(r,c, parent_r, parent_c):
            if (r,c) in visit:
                return
            visit.add((r,c))

            for dr,dc in directions:
                row = r + dr
                col = c + dc
                if row not in range(rows) or col not in range(cols) or grid[row][col] != grid[r][c]:
                    continue
                if (row, col) == (parent_r, parent_c):
                    continue

                if (row,col) in visit: # visit a cell that aready visited and NOT the parent --> cycle
                    return True
                if dfs(row,col,r,c):
                    return True
            return False
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visit:
                    if dfs(r,c,-1,-1):
                        return True
        return False





        