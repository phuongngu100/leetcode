class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        graph = [[] for _ in range(n + 1)]

        # Build graph
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        colors = [-1] * (n+1)

        for p in range(1,n+1):
            if colors[p] != -1:
                continue
            colors[p] = 0
            q = deque([p])
            while q:
                node = q.popleft()
                for nei in graph[node]:
                    # Neighbor hasn't been assigned a group
                    if colors[nei] == -1:
                        colors[nei] = 1 - colors[node]
                        q.append(nei)
                    # Neighbor is in the same group -> impossible
                    elif colors[nei] == colors[node]:
                        return False

        return True



        