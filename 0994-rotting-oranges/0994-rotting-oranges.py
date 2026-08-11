class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        q = collections.deque()

        fresh, time = 0,0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        while fresh > 0 and q: # when there are fresh oranges to be rotten and when there existed at least a rotten orange, we start to pop from the queue
            for i in range(len(q)):
                r,c = q.popleft()
                for dr, dc in directions: # check all directions
                    row, col = r+dr, c+dc
                    # check if they're in range and if it's an orange not an empty cell
                    if (row in range(rows) and col in range(cols) and grid[row][col] == 1):
                        grid[row][col] = 2
                        q.append((row,col))
                        fresh -= 1
            # after the loop, increase the time
            time += 1
        return time if fresh == 0 else -1


                



        