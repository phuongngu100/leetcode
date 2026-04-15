class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        res = 0
        costs.sort(key=lambda x : x[0]-x[1]) #pricea - price b

        n = len(costs) // 2

        for i in range(n):
            res += costs[i][0] + costs[i+n][1] # first half sends to citya, second half sends to cityb
        return res
