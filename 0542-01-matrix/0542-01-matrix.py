class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])

        q = collections.deque()

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    q.append((r,c))
                else:
                    mat[r][c] = -1
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                row, col = r + dr, c + dc
                if (row in range(rows) and col in range(cols) and mat[row][col] == -1):
                    mat[row][col] = mat[r][c] + 1 # so the current cell we're looking at is mat[r][c], we want to plus 1 to the neighbor, which is mat[row][col]; example mat[r][c] = 0 then we want its neighbor to be 0 + 1 = 1, if 1 then 1 + 1 = 2
                    q.append((row,col))
        return mat
        