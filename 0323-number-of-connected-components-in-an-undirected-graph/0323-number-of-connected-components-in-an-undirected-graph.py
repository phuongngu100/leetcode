class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        components = n
        def union(a,b):
            nonlocal components
            root_a, root_b = find(a), find(b)
            # If the roots are different, a and b are currently
            # in two DIFFERENT components.
            if root_a != root_b:

                # Connect the two components by making
                # root_b the parent of root_a.
                parent[root_a] = root_b

                # Two components have now become one,
                # so decrease the component count by 1.
                components -= 1
        
        for a,b in edges:
            union(a,b)
        return components

