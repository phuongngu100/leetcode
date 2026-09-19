class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []

        def backtrack(perm, i):
            if len(perm) == k:
                res.append(perm.copy())
                return

            for num in range(i, n+1):
                perm.append(num)
                backtrack(perm, num+1)
                perm.pop()
        backtrack([], 1)
        return res
        # time O(k * C(n,k)); since copy takes k and there are C(n.k) combinations
        # space: also the same cause C(n,k) combinations of size k