class Leaderboard:

    def __init__(self):
        self.scores = {} # a dictionary with playerID as key and score as value

    def addScore(self, playerID: int, score: int) -> None:
        if playerID not in self.scores:
            self.scores[playerID] = 0
        self.scores[playerID] += score

    def top(self, K: int) -> int:
        # using heap, min heap is a python default
        heap = []
        for x in self.scores.values():
            heapq.heappush(heap,x) # push into heap the value x
            if len(heap) > K: # if more than k, dont need anymore --> pop
                heapq.heappop(heap)
        res = 0
        while heap:
            res += heapq.heappop(heap)
        return res

    def reset(self, playerID: int) -> None:
        self.scores[playerID] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)