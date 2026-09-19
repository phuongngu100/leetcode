class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        res = []
        count = {n:0 for n in nums} # initiate 0 for all n in nums
        for n in nums:
            count[n] += 1

        def backtrack(perm):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            for num in count:
                if count[num] > 0:
                    perm.append(num)
                    count[num] -=1
                    backtrack(perm)
                    count[num] +=1
                    perm.pop()
            
        backtrack([])
        return res
            