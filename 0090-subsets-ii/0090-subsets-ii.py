class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        def backtrack(subset, i):
            res.append(subset.copy())
            # choice 1: to include the number
            for j in range(i, len(nums)):
                if nums[j] == nums[j-1] and j > i:
                    continue
                subset.append(nums[j]) # if chosen, add to the subset
                backtrack(subset, j+1)
                subset.pop()

            # choice 2: to not include it
            # backtrack(subset, i+1)
        backtrack([],0)
        return res



