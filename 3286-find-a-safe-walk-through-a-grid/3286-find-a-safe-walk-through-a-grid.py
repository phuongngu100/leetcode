class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        rows = len(grid)
        cols = len(grid[0])

        dis = [[float('inf')] * cols for _ in range(rows)] # inf to mark unvisited
        dis[0][0] = grid[0][0]
        heap = [(grid[0][0],0,0)]

        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        while heap:
            cost,r,c = heapq.heappop(heap) # the heap gives the smallest cost
            if cost > dis[r][c]: # theres a better path, like find a 1 instead of 0; if its 0 and 0, which means 0 is not > 0, then continue like normal
                continue
            if r == rows - 1 and c == cols - 1: #reach destination
                return health - cost >=1 # return only if health is >= 1
            for dr, dc in directions:
                row, col = r+dr, c+dc

                if (row in range(rows) and col in range(cols)):
                    new_cost = cost + grid[row][col]
                    if new_cost < dis[row][col]: 
                        dis[row][col] = new_cost
                        heapq.heappush(heap, (new_cost,row,col))
        return False

            
        
                
                
        