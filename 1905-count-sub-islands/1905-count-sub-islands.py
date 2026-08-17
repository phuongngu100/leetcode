class Solution:
    directions = [[0,1],[0,-1],[1,0],[-1,0]]

    def isCellland(self, r,c,grid):
        if grid[r][c] == 1:
            return True
        return False
    def isSubIsland(self,r,c,grid1, grid2, visited):
        rows, cols = len(grid2), len(grid2[0])

        isSubIsland = True 
        q = deque()
        q.append((r,c))
        visited.add((r,c))
        while q:
            row,col = q.popleft()
            if not self.isCellland(row,col,grid1):
                isSubIsland = False
            for dr, dc in self.directions:
                nr,nc = dr+row, dc+col
                if (nr in range(rows) and nc in range(cols) and (nr,nc) not in visited and self.isCellland(nr,nc,grid2)):
                    q.append((nr,nc))
                    visited.add((nr,nc))
        return isSubIsland


    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid2), len(grid2[0])
        # direcctions = [[0,1],[0,-1],[1,0],[[-1,0]]]
        visited = set()
        subIslandsCount = 0
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and self.isCellland(r,c,grid2) and self.isSubIsland(r,c,grid1, grid2, visited):
                    subIslandsCount += 1
        return subIslandsCount







        