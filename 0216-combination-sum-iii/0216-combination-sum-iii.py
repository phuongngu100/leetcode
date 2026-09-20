class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        res = []

        def backtrack(sub, total, start):
       
            if len(sub) == k:
                if total == n:
                    res.append(sub.copy())
                    return
            for i in range(start,10):
                if total + i > n:
                    continue
              
                sub.append(i)
                backtrack(sub,total+i, i+1)
                sub.pop()
        
        backtrack([], 0, 1)
        return res
                



        