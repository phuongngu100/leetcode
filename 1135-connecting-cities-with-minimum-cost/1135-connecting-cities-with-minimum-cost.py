class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        graph = [[] for _ in range(n+1)]
        for x, y, cost in connections:
            graph[x].append((y,cost))
            graph[y].append((x,cost))
        
        heap = [(0,1)] # cost, city
        visited = set()
        total = 0

        while heap:
            cost, city = heapq.heappop(heap)
            if city in visited:
                continue
            visited.add(city)
            total += cost
            if len(visited) == n:
                return total
            for nei, price in graph[city]:
                if nei not in visited:
                    heapq.heappush(heap,(price, nei))
        return -1


