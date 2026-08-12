class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        heap = [(0, src, 0)] # cost, src, number of stops
        graph = [[] for _ in range(n)]
        for fr, to, price in flights:
            graph[fr].append((to,price))
        dist = [[float('inf')]*(k+2) for _ in range(n)] # + 2 for 
        dist[src][0] = 0 # example: dist[2][1] means we visit 2 cities with 1 flight
        '''
        dist[city][number of flights] = cheapest price
        For every city, I'm keeping track of the cheapest price I've found for each possible number of flights.
                    NUMBER OF FLIGHTS
                    0     1     2     3
                ┌─────┬─────┬─────┬─────┐
        city 0     │  0  │  ∞  │  ∞  │  ∞  │
        city 1     │  ∞  │ 100 │  ∞  │  ∞  │
        city 2     │  ∞  │ 500 │ 200 │  ∞  │
        city 3     │  ∞  │  ∞  │  ∞  │ 300 │
                └─────┴─────┴─────┴─────┘
        '''

        while heap:
            cost, city,stops = heapq.heappop(heap) # first we have 0,0,0, meaning from city 0 to 0 take 0 flights
            if city == dst:
                return cost
            if stops >= k+1: # cant take more flight
                continue
            for nei, price in graph[city]:
                new_cost = cost + price
                new_stops = stops + 1 # add 1 more stop
                if new_cost < dist[nei][new_stops]:
                    dist[nei][new_stops] = new_cost
                    heapq.heappush(
                        heap,
                        (new_cost, nei, new_stops)
                    )
        return -1
        