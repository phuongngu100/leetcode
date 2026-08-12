class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        heap = [(0, 0, 0)] # cost, start, discount used
        graph = [[] for _ in range(n)]
        for a, b, toll in highways: # since this is bidirectional
            graph[a].append((b, toll))
            graph[b].append((a, toll))
        dist = [[float('inf')] * (discounts+1) for _ in range(n)]
        dist[0][0] = 0

        while heap:
            cost, city, used = heapq.heappop(heap)
            if city == n-1:
                return cost
            if cost > dist[city][used]:
                continue
            for nei, toll in graph[city]:
                # option 1: dont use discount
                new_cost = cost + toll
                if new_cost < dist[nei][used]:
                    dist[nei][used] = new_cost
                    heapq.heappush(heap, (new_cost,nei,used))
         
                # option 2: use discount
                if used < discounts:
                    new_cost = cost + toll//2
                    new_used = used + 1
                    if new_cost < dist[nei][new_used]: # we only update if using the discount is cheaper
                        dist[nei][new_used] = new_cost
                        heapq.heappush(heap, (new_cost,nei,new_used))
        return -1



        