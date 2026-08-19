class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n+1)]
        # --------------------------------------------------
        # STEP 1: Dijkstra from node n
        # distance[x] = shortest distance from x to node n
        # --------------------------------------------------
        for u,v,w in edges:
            graph[u].append((v,w))
            graph[v].append((u,w))
        distance = [float('inf')]*(n+1)
        distance[n] = 0 # distance from n to n is 0
        heap = [(0, n)] # distance, node n

        while heap:
            dist, node = heapq.heappop(heap)
            if dist > distance[node]:
                continue
            for nei, d in graph[node]:
                new_d = d + dist
                if new_d < distance[nei]:
                    distance[nei] = new_d
                    heapq.heappush(heap,(new_d, nei))
        
        # --------------------------------------------------
        # STEP 2: Count restricted paths using DFS + memoization
        # --------------------------------------------------

        memo = [None] *(n+1)
        def dfs(node):
            # We reached node n: exactly one path exists
            if node == n:
                return 1
            # Already calculated this node
            if memo[node] is not None:
                return memo[node]
            count = 0

            # Only move to a node with a smaller shortest distance
            for nei, d in graph[node]:
                if distance[node] > distance[nei]:
                    count += dfs(nei)
                    count %= (10**9+7)

            memo[node] = count
            return count

        return dfs(1)