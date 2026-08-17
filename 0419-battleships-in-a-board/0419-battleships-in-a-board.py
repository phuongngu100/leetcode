class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board: return
        rows, cols = len(board), len(board[0])
        battleships = 0

        def dfs(r,c):
            if (r not in range(rows) or c not in range(cols) or board[r][c] != 'X'):
                return
            board[r][c] = '.'
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'X':
                    dfs(r,c)
                    battleships += 1
        return battleships




        