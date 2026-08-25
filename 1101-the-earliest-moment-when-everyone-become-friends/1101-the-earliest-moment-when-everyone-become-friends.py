class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort()
        parent = list(range(n))
        components = n

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(a,b):
            nonlocal components

            root_a,root_b = find(a), find(b)
            if root_a == root_b:
                return
            parent[root_a] = root_b
            components -= 1

        for time, i, j in logs:
            union(i,j)
            if components == 1:
                return time
        return -1