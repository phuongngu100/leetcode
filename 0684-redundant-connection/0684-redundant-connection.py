class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        graph = [[] for _ in range(n+1)]

        # for a, b in edges:
        #     edges[a].append(b)
        #     edges[b].append(a)
        
        def dfs(node, parent, target):
            if node == target:
                return True
            visit.add(node)
            for nei in graph[node]:
                if nei == parent or nei in visit:
                    continue
                if dfs(nei, node, target):
                    return True
            return False
        for a,b in edges:
            visit = set()
            # If a and b are already connected,
            # adding this edge creates a cycle
            if dfs(a, -1, b):
                return [a, b]
            # Otherwise, safely add the edge
            graph[a].append(b)
            graph[b].append(a)


        