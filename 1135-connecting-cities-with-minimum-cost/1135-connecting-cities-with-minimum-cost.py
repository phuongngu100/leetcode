class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        # this is a bidirectional; create a graph to map all the to and from
        graph = [[] for _ in range(n+1)]
        for x,y,cost in connections:
            graph[x].append((y,cost))
            graph[y].append((x,cost))

        # how to know that all the cities are connected? keep track of all the cities we have visited, if we reach the given city number, that means all are connected
        visited = set()
        # create a heap to keep track of the cheapest cost
        heap = [(0, 1)] # cost, current city
        total = 0 # we need to accumulate all the cost
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
                    heapq.heappush(heap, (price, nei))   
        return -1             




















        # graph = [[] for _ in range(n+1)]
        # for x, y, cost in connections:
        #     graph[x].append((y,cost))
        #     graph[y].append((x,cost))
        
        # heap = [(0,1)] # cost, city
        # visited = set()
        # total = 0

        # while heap:
        #     cost, city = heapq.heappop(heap)
        #     if city in visited:
        #         continue
        #     visited.add(city)
        #     total += cost
        #     if len(visited) == n:
        #         return total
        #     for nei, price in graph[city]:
        #         if nei not in visited:
        #             heapq.heappush(heap,(price, nei))
        # return -1


