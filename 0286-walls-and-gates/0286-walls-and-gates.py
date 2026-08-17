class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows = len(rooms)
        cols = len(rooms[0])

        q = collections.deque()
        # visited = set()

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    q.append((r,c))
                    # visited.add((r,c))
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        while q:
            r,c = q.popleft()
            for dr,dc in directions:
                row, col = r+dr, c+dc
                if (row in range(rows) and col in range(cols) and rooms[row][col] == 2147483647): # dont actually need visited because we can know its not visited by it being iINF
                    rooms[row][col] = rooms[r][c] + 1
                    # visited.add((row,col))
                    q.append((row,col))

            
















        # rows = len(rooms)
        # cols = len(rooms[0])
        # q = collections.deque()
        # visited = set()
        # def bfs(r,c):
        #     if (r not in range(rows) or c not in range(cols) or rooms[r][c] == -1 or (r,c) in visited):
        #         return
        #     visited.add((r,c))
        #     q.append((r,c))



        # for r in range(rows):
        #     for c in range(cols):
        #         if rooms[r][c] == 0:
        #             visited.add((r,c))
        #             q.append((r,c))
        # dist = 0
        # while q:
        #     for i in range(len(q)):
        #         r,c = q.popleft()
        #         rooms[r][c] = dist
        #         bfs(r+1,c)
        #         bfs(r-1,c)
        #         bfs(r,c+1)
        #         bfs(r,c-1)
        #     dist+=1

