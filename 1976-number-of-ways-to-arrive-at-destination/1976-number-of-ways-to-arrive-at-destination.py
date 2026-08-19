class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        path = [[] for _ in range(n)]
        for u,v,time in roads:
            path[u].append((v,time))
            path[v].append((u,time))
        
        heap = [(0, 0)] # time, start aka city 0 
        path_count = [0] * n # number of ways to reach that node in the shortest time
        path_count[0] = 1 # there is 1 way to go from 0 to 0
        shortest_time = [float('inf')] * n # shortest time to reach each node
        shortest_time[0] = 0 # shortest time to reach node 0 is 0

        while heap:
            time, node = heapq.heappop(heap)
            if time > shortest_time[node]:
                continue
            # if node == n - 1:
            #     return path_count[n-1] # unnecessary bc reach the node doesnt mean we have counted all the ways
            for nei, t in path[node]:
                new_time = t + time
                if new_time < shortest_time[nei]:
                    shortest_time[nei] = new_time
                    path_count[nei] = path_count[node]
                    heapq.heappush(heap, (new_time, nei))
                elif new_time == shortest_time[nei]:
                    # shortest_time[nei] = new_time
                    path_count[nei] = (path_count[nei] + path_count[node])  % (10**9 + 7)
                
        return path_count[n-1]
            




        