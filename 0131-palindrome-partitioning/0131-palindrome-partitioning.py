class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []

        def backtrack(substring,i):
            if i >= len(s):
                res.append(substring.copy())
                return
            for j in range(i, len(s)):
                if self.isPali(s,i,j):
                    substring.append(s[i:j+1])
                    backtrack(substring, j+1)
                    substring.pop()
        backtrack([],0)
        return res





    def isPali(self, s,l,r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l+1, r-1
        return True
