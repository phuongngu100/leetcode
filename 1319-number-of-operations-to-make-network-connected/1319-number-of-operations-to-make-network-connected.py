class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        # print(parent)
        components = n
        count = 0

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(a,b):
            nonlocal components
            
            root_a = find(a)
            root_b = find(b)

            if root_a == root_b:
                return False

            parent[root_a] = root_b
            components -= 1
            return True

        for a,b in connections:
            if not union(a,b):
                count += 1
        if count >= components - 1:
            return components -1
        return -1

        

            

        