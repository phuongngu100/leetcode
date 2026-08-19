class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n+1)]
        for u,v,time in times:
            graph[u].append((v,time))
        
        heap = [(0, k)] #time, starting node
        visit = set()
        total = 0
        distance = [float('inf')]*(n+1) # 1-indexed
        distance[k] = 0


        while heap:
            time, node = heapq.heappop(heap)
            if node in visit:
                continue
            visit.add(node)
            if time > distance[node]:
                continue
            if len(visit) == n:
                return time
            for nei, t in graph[node]:
                new_time = t + time
                if new_time < distance[nei]:
                    distance[nei] = new_time
                    heapq.heappush(heap,(new_time, nei))
        return -1
            

