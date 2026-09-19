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
        