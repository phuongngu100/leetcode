class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        jset = set(jewels)
        for i in stones:
            if i in jset:
                res += 1
        return res

        