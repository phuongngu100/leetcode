class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = list(range(n))
        components = n

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(a,b):
            nonlocal components
            root_a, root_b = find(a), find(b)
            if root_a == root_b:
                return False # found a cycle
            parent[root_a] = root_b
            components -= 1
            return True

        for a,b in edges:
            if not union(a,b):
                return False
        print(components)
        return components == 1

        