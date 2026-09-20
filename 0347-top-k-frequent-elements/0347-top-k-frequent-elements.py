class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        count = {}
        res = []
        for n in nums:
            count[n] = count.get(n,0) + 1
        for key, val in count.items():
            heapq.heappush(heap,(-val,key))
        while len(res) < k:
            res.append(heapq.heappop(heap)[1])
        return res
        