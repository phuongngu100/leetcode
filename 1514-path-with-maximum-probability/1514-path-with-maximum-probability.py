class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        res = 0
        path = [[] for _ in range(n)]
        for i in range(len(edges)):
            a,b = edges[i]
            success_prob = succProb[i]
            path[a].append((b,success_prob))
            path[b].append((a,success_prob))
            # we want the largest, hence the negative
        heap = [(-1.0, start)] # prob, start
        # best probability found in each node
        best = [0.0]*n
        best[start] = 1.0

        
        while heap:
            neg_p, cur = heapq.heappop(heap)
            p = - neg_p
            if cur == end:
                return p
            if p < best[cur]: # ignore if p is smaller
                continue
            for nei, prob in path[cur]:
                new_prob = prob * p
                if new_prob > best[nei]:
                    best[nei] = new_prob
                    heapq.heappush(heap,(-new_prob,nei))
        return 0.0








        