class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        distance = [[float('inf')]*cols for _ in range(rows)]

        # Starting position has distance 0
        distance[start[0]][start[1]] = 0
        heap = [(0, start[0], start[1])] # dis, row, col
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        while heap:
            dist, r, c = heapq.heappop(heap)
            if dist > distance[r][c]:
                continue
            if [r,c] == destination:
                return dist
            # rey rolling in all direction
            for dr, dc in directions:
                new_dist = dist
                # row, col = r+dr, c+dc 
                # think of the rolling as
                row, col = r,c # start at the current stopping position
                while (row+dr in range(rows) and col+dc in range(cols) and maze[row+dr][col+dc] == 0):
                    row += dr
                    col += dc
                    new_dist +=1
                if new_dist < distance[row][col]:
                    distance[row][col] = new_dist
                    heapq.heappush(heap, (new_dist, row, col))
        return -1




       

