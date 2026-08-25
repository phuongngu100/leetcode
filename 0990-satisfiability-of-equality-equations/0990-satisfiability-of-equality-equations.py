class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        root = list(range(26))
        print(root)          
        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]
        
        def union(a,b):
            a, b = find(a), find(b)
            root[a] = b
        for e in equations:
            if e[1] == '=':
                a, b  = ord(e[0])-ord('a'), ord(e[3])-ord('a') # convert letters into number to match the roots
                union(a,b)
        for e in equations:
            if e[1] == '!':
                a, b  = ord(e[0])-ord('a'), ord(e[3])-ord('a') # convert letters into number to match the roots

                if find(a) == find(b):
                    return False
        return True

            
            
