class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # use dfs to explore all path aka finding province
        prov = 0
        stack = []

        # rows = len(isConnected)
        # cols = len(isConnected[0])
        # not needed because this is a n x n matrx not n x m
        n = len(isConnected)

        def dfs(city):
            stack.append(city)
            for i in range(n):
                if isConnected[city][i] == 1 and i not in stack:
                    dfs(i)
        for city in range(n):
            if city not in stack:
                prov += 1
                dfs(city)

        return prov
        