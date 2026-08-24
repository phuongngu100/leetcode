class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        def find(x):
            if parent[x] != x:
                x = find(parent[x])
            return parent[x]
        def union(a,b):
            root_a = find(a)
            root_b = find(b)

            # if find a cycle
            if root_a == root_b:
                return False
            parent[root_a] = root_b
            return True
        
        for a,b in edges:
            if not union(a,b):
                return [a,b]










        # n = len(edges)
        # graph = [[] for _ in range(n+1)]
        
        # def dfs(node, parent, target):
        #     if node == target:
        #         return True
        #     visit.add(node)
        #     for nei in graph[node]:
        #         if nei == parent or nei in visit:
        #             continue
        #         if dfs(nei, node, target):
        #             return True
        #     return False
        # for a,b in edges:
        #     visit = set()
        #     # If a and b are already connected,
        #     # adding this edge creates a cycle
        #     if dfs(a, -1, b):
        #         return [a, b]
        #     # Otherwise, safely add the edge
        #     graph[a].append(b)
        #     graph[b].append(a)


        