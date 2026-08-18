class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        rows, cols = len(land), len(land[0])
        visit = set()
        farmland = []

        def dfs(r,c):
            if (r not in range(rows) or c not in range(cols) or land[r][c] != 1 or (r,c) in visit):
                return
            visit.add((r,c))

            # keep track of the minimum rows and cols encountered
            nonlocal min_row, min_col, max_row, max_col
            min_row = min(min_row,r)
            min_col = min(min_col,c)
            max_row = max(max_row,r)
            max_col = max(max_col,c)

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        for r in range(rows):
            for c in range(cols):
                if land[r][c] == 1 and (r,c) not in visit:
                    min_row = float('inf')
                    min_col = float('inf')
                    max_row = float('-inf')
                    max_col = float('-inf')

                    dfs(r,c)

                    farmland.append((min_row,min_col,max_row,max_col))
        return farmland






            
        